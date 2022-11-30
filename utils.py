import json
import numpy as np

def redistribute_flux(filter_orig, filter_new, ab_mag_orig, verbose=False):

	'''
	filter_orig: string
	path to original filter transmission data

	filter_new: string
	path to new filter transmission data

	ab_mag_orig: float
	magnitude measured using original filter

	verbose: bool
	if true, prints detailed information about the conversion
	'''

	import numpy as np
	from scipy.integrate import simps

	# Load the filter data
	f1 = np.loadtxt(filter_orig, dtype='float')
	f2 = np.loadtxt(filter_new, dtype='float')

	# Identify the wavelength range the 2 filters share in common
	wav_low = np.max([np.min(f1[:, 0]), np.min(f2[:, 0])])
	wav_upp = np.min([np.max(f1[:, 0]), np.max(f2[:, 0])])
	if verbose: print('Wavelength range: %g to %g Angstroms' % ( wav_low, wav_upp ))

	# Restrict the filter data to the common shared wavelengths
	f1_wavs = np.where((f1[:, 0] > wav_low) & (f1[:, 0] < wav_upp))[0]
	f2_wavs = np.where((f2[:, 0] > wav_low) & (f2[:, 0] < wav_upp))[0]
	f1 = f1[f1_wavs, :]
	f2 = f2[f2_wavs, :]

	# Integrate filter transmission data to get transmission ratio
	# Simpson's rule integral takes arguments simpson(y, x)
	# We want f2/f1 since flux_f2 = f2/f1*flux_f1
	f1_intgrl = simps(f1[:, 1], f1[:, 0])
	f2_intgrl = simps(f2[:, 1], f2[:, 0])
	ratio = f2_intgrl/f1_intgrl
	if verbose: print('Flux ratio f2/f1: ', ratio)
	
	# Convert AB magnitude observation back to flux
	# Scale the flux by the integrated filter transmission ratio
	# Re-convert flux back to AB mag to get the observation in the new filter
	flux = 10**((ab_mag_orig+48.6)/-2.5)
	flux *= ratio
	ab_mag_new = -2.5*np.log10(flux)-48.6
	if verbose: print('New AB mag: ', ab_mag_new)

	return ab_mag_new
	
def update_photometry(dfile, times, f1, f2, old_obs, obs_idxs, new_band, old_band, instrument, telescope, delete_flags, convert_from_vega=False): 
	'''
	dfile: string
	path to GRB050709.json data file

	times: float
	observation time in MJD at which the *new observation* will be recorded
	
	f1: string
	path to the *original* filter transmission data

	f2: string
	path to the *new* filter transmission data

	old_obs: float
	old observation magnitude measurement

	new_band: string
	filter name of new band (i.e. grizyJHK, F814W, etc.)

	old_band: string
	filter name of old band (i.e. grizyJHK, F814W, etc.)

	instrument: string
	name of instrument which houses the *new* filter

	telescope: string
	name of telescope which houses the *new* filter

	delete_flags: bool
	boolean flag for whether or not to delete an old observation.
	set True for the first occurrence of each observation time.
	for example:
	the V-band can be broken down into the g- and r-bands.
	when adding the g-band observation, we set delete_flags = True
	which deletes the old V-band observation.
	for the r-band observation, we set delete_flags = False
	since the old V-band observation has already been removed.
	'''

	# These magnitudes are reported using the VEGA magnitude system
	# As such, the new magnitudes are converted to AB magnitude values using the offset values in reference
	# m_AB - m_vega = offset
	# m_AB = offset + m_vega
	# Reference: https://www.astronomy.ohio-state.edu/martini.10/usefuldata.html

	offsets = {
		"g": -0.08,
		"r": 0.16,
		"i": 0.37,
		"z": 0.54,
		"y": 0.63,
		"J": 0.91,
		"H": 1.39,
		"K": 1.85}

	data = json.load(open(dfile), encoding="UTF-8")
	photometry = data[dfile.split('/')[-1][:-5]]["photometry"]
	## Each N added observations will shift the old observation indices by N-1 (the -1 is from removing the old observations), so we add counter
	counter = 1
	obs_times = np.array([float(photometry[entry]["time"]) for entry in range(len(photometry))])
	for i in range(len(times)):
		#obs_idx = np.argmin(np.abs(times[i]-obs_times)) # this fails if two observations share a common time
		obs_idx = obs_idxs[i]
		old_photometry = photometry[obs_idx+counter-1]
		if delete_flags[i]:
			photometry = np.delete(photometry, obs_idx+counter-1).tolist()
			counter -= 1
		# Calculate magnitude in new filter
		new_mag = redistribute_flux('filters/'+f1[i], 'filters/'+f2[i], old_obs[i])
		if convert_from_vega: new_mag += offsets[new_band[i]] # Vega -> AB conversion

		# Update dictionary entries with new band information
		new_obs_band = old_photometry.copy()
		new_obs_band["magnitude"] = str(round(new_mag, 1))
		new_obs_band["band"] = new_band[i]
		new_obs_band["instrument"] = instrument[i]
		new_obs_band["telescope"] = telescope[i]
		new_obs_band["system"] = "AB"
		new_obs_band["source"] = "converted from %s-band observation" % old_band[i]
		photometry = np.insert(photometry, obs_idx+counter, new_obs_band).tolist()
		counter += 1
	
	photometry = adjust_filters(photometry)
	data[dfile.split('/')[-1][:-5]]["photometry"] = photometry
	with open('kne-parsed/%s_updated_obs.json' % dfile.split('/')[-1][:-5], 'w') as f:
		json.dump(data, f, ensure_ascii=True, indent=4)

def adjust_filters(photometry):
	
	filters = {
		"g": "g",
		"r": "r",
		"i": "i",
		"z": "z",
		"y": "y",
		"J": "J",
		"H": "H",
		"K": "K",
		"R": "r",
		"Ks": "K",
		"I": "i",
		"r'": "r",}

	for obs in photometry:
		obs["band"] = filters[obs["band"]]
		if "e_magnitude" in obs.keys(): continue
		elif ("e_upper_magnitude" in obs.keys() and "e_lower_magnitude" in obs.keys()):
			obs["e_magnitude"] = str(np.mean([float(obs["e_lower_magnitude"]), float(obs["e_upper_magnitude"])]))
		elif obs["upperlimit"] == True:
			obs["e_magnitude"] = str(2)
	
	return photometry
