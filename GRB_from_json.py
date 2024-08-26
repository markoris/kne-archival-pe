import json
import numpy as np

class GRB:

	def __init__(self, path_to_GRB_json): 

		import json

		self.name = path_to_GRB_json.split('/')[-1][:-5]
		self.jsondata = json.load(open(path_to_GRB_json))
		self.photometry = self.jsondata[self.name]["photometry"]

		# These magnitudes are reported using the VEGA magnitude system
		# As such, the new magnitudes are converted to AB magnitude values using the offset values in reference
		# m_AB - m_vega = offset
		# m_AB = offset + m_vega
		# Reference: https://www.astronomy.ohio-state.edu/martini.10/usefuldata.html

		self.sim_filters = ['lsstg', 'lsstr', 'lssti', 'lsstz', 'lssty',
					'2massJ', '2massH', '2massK']

		self.vega_offsets = {
			"lsstg": -0.08,
			"lsstr": 0.16,
			"lssti": 0.37,
			"lsstz": 0.54,
			"lssty": 0.63,
			"2massJ": 0.91,
			"2massH": 1.39,
			"2massK": 1.85}

		# all filter data acquired from SVO Filter Profile Service

		self.fmap = {
			# Original observation filters
			# GRB130603B
			'CAHA.DLR-MKIII.V': 'CAHA.DLR-MKIII.V',  ### GENERIC
			'GTC.OSIRIS.r': 'GTC/OSIRIS.sdss_r_filter',
			'Gemini-North.GMOS.g': 'Gemini/GMOS-N.g', 
			'Gemini-North.GMOS.i': 'Gemini/GMOS-N.i',
			'Gemini-North.GMOS.r': 'Gemini/GMOS-N.r',
			'Gemini-North.GMOS.z': 'Gemini/GMOS-N.z',
			'Gemini-South.GMOS.g': 'Gemini/GMOS-S.g',
			'Gemini-South.GMOS.i': 'Gemini/GMOS-S.i',
			'Gemini-South.GMOS.r': 'Gemini/GMOS-S.r',
			'HST.ACS.F606W': 'HST/ACS_WFC.F606W', 		# Full instrument throughput
			'HST.WFC3.F160W': 'HST/WFC3_IR.F160W', 		# Full instrument throughput
			'MMT.MMTCam.r': 'MMT/MMTCam.r',
			'Magellan/Baade.IMACS.r': 'LCO/IMACS.sloan_r',
			'Magellan/Clay.LDSS3.r': 'LCO/IMACS.sloan_r', ### Could not find unique Clay filter, using Baade as proxy
			'NOT.MOSCA.r': 'NOT.MOSCA.r', ### Obtained NOT.MOSCA.r Gunn r filter from https://www.not.iac.es/instruments/filters/filters.php
			'Swift.UVOT.V': 'Swift/UVOT.V',
			'TNG.DOLoRes.i': 'TNG/DOLORES.SDSS_i',
			'TNG.DOLoRes.r': 'TNG/DOLORES.SDSS_r',
			'UKIRT.WFCAM.J': 'UKIRT/WFCAM.J_filter',
			'UKIRT.WFCAM.K': 'UKIRT/WFCAM.K_filter',
			'VLT.HAWK-I.J': 'Paranal/HAWKI.J',
			'WHT.ACAM.g': 'WHT/ULTRACAM.g_filter', ### Could not find ACAM on WHT website, using ULTRACAM as proxy
			'WHT.ACAM.i': 'WHT/ULTRACAM.i_filter', ### Could not find ACAM on WHT website, using ULTRACAM as proxy
			'WHT.ACAM.z': 'WHT/ULTRACAM.z_filter', ### Could not find ACAM on WHT website, using ULTRACAM as proxy
			# GRB150101B
			'Gemini.GMOS.r': 'Gemini/GMOS-S.r',
			'HST.WFC3.F160W': 'HST/WFC3_IR.F160W',
			'HST.WFC3.F606W': 'HST/WFC3_UVIS1.F606W',
			'Magellan.IMACS.r': 'HST/WFC3_UVIS1.F606W',
			'VLT.HAWK-I.J': 'Paranal/HAWKI.J',
			# GRB160821B
			'GTC.OSIRIS.g': 'GTC/OSIRIS.sdss_g_filter',
			'GTC.OSIRIS.i': 'GTC/OSIRIS.sdss_i_filter',
			'GTC.OSIRIS.r': 'GTC/OSIRIS.sdss_r_filter',
			'GTC.OSIRIS.z': 'GTC/OSIRIS.sdss_z_filter',
			'HST.WFC3.F110W': 'HST/WFC3_IR.F110W',
			'HST.WFC3.F160W': 'HST/WFC3_IR.F160W',
			'HST.WFC3.F606W': 'HST/WFC3_UVIS1.F606W',
			'KeckI.MOSFIRE.Ks': 'Keck/NIRC2.Ks', 	### Could not find MOSFIRE, but NIRC2 is very similar
			# GRB211211A
			"CAHA.CAFOS.g'": 'TNO/ULTRACAM.g-3', # Could not find exact match, using close substitute 
			'CAHA.CAFOS.i': 'TNO/ULTRACAM.i-3', # Could not find exact match, using close substitute
			"CAHA.CAFOS.i'": 'TNO/ULTRACAM.i-3', # Could not find exact match, using close substitute
			"CAHA.CAFOS.r'": 'TNO/ULTRACAM.r-3', # Could not find exact match, using close substitute
			'DOT.IMAGER.B': 'DOT.IMAGER.B',
			'DOT.IMAGER.I': 'DOT.IMAGER.I',
			'DOT.IMAGER.R': 'DOT.IMAGER.R',
			'DOT.IMAGER.U': 'DOT.IMAGER.U',
			'DOT.IMAGER.V': 'DOT.IMAGER.V',
			'Gemini.NIRI.K': 'Gemini/NIRI.K-G0204w',
			'MMT.MMIRS.K': 'MMT/MMIRS.Ks',
			'OAO.MITSUME.Ic': 'OAO/KOOLS.Ic_filter', # Using KOOLS filter-only as proxy
			'OAO.MITSUME.Rc': 'OAO/KOOLS.Rc_filter', # Using KOOLS filter-only as proxy
			'OAO.MITSUME.g': 'OAO/KOOLS.sdss_g_filter', # Using KOOLS filter-only as proxy
			'Swift.UVOT.b': 'Swift/UVOT.B_fil',
			'Swift.UVOT.m2': 'Swift/UVOT.UVM2_fil',
			'Swift.UVOT.u': 'Swift/UVOT.U_fil',
			'Swift.UVOT.w1': 'Swift/UVOT.UVW1_fil',
			'Swift.UVOT.w2': 'Swift/UVOT.UVW2_fil',
			#GRB230307A
			'CTIO.KMTNet.I': 'CTIO.KMTNet.I', 	### Generic
			'CTIO.KMTNet.R': 'CTIO.KMTNet.R', 	### Generic
			'ElSauce.RASA36.r' : 'ElSauce.RASA36.R', ### Generic
			'Gemini.GMOS-S.r': 'Gemini/GMOS-S.r',
			'Gemini.GMOS-S.z': 'Gemini/GMOS-S.z',
			'SAAO.KMTNet.I': 'SAAO.KMTNet.I', 	### Generic
			'SAAO.KMTNet.R': 'SAAO.KMTNet.R',
			'SAAO.PRIME.H': '2MASS/2MASS.H', ### Calibrated to 2MASS per Yang 2024 Nature paper 
			'SAAO.PRIME.J': '2MASS/2MASS.J', ### Calibrated to 2MASS per Yang 2024 Nature paper
			'SAAO.PRIME.Y': 'Paranal/VISTA.Y_filter', ### Calibrate to VISTA per Yang 2024 Nature paper
			"SOAR.GHTS.z'": 'TNO/ULTRACAM.z-3', ### Could not find exact match, using close substitute 
			'SSO.KMTNet.I': 'SSO.KMTNet.I', 	### Generic
			'SSO.KMTNet.R': 'SSO.KMTNet.R', 	### Generic
			'Swift.UVOT.u': 'Swift/UVOT.U_fil',
			'Swift.UVOT.white': 'Swift/UVOT.white_fil',
			'TESS.TESS.Red': 'TESS/TESS.Red',
			'VLT.XSH.K': 'Paranal/HAWKI.Ks', # Use HAWK-I Ks band as proxy, no Xshooter filter data
			# Destination filters
			'lsstg': 'LSST/LSST.g',
			'lsstr': 'LSST/LSST.r',
			'lssti': 'LSST/LSST.i',
			'lsstz': 'LSST/LSST.z',
			'lssty': 'LSST/LSST.y',
			'2massJ': '2MASS/2MASS.J',
			'2massH': '2MASS/2MASS.H',
			'2massK': '2MASS/2MASS.Ks'
			}

		return

	def get_filter_key(self, observation):
			# construct filter keys as in get_filters()	
			try: 
				return observation['telescope']+'.'+observation['instrument']+'.'+observation['band']
			# sometimes the telescope is included with the instrument
			except KeyError: return observation['instrument']+'.'+observation['band']

	def get_obs_sources(self):
		'''
		Prints a list of dictionary keys generated by concatenating
		the observation['telescope']+observation['band'] strings for
		each observation in the photometry dictionary.
		'''

		# create empty list to house instrument+band combinations
		all_filters = []

		# loop over all observations in the photometry dictionary
		for observation in self.photometry:
			try: all_filters.append(observation['telescope']+'.'+observation['instrument']+'.'+observation['band'])
			# sometimes the telescope is included with the instrument
			except KeyError: all_filters.append(observation['instrument']+'.'+observation['band'])

		# Return all observations, removing duplicate instrument+band combinations
		return np.unique(all_filters)

	def redistribute_flux(self, filter_orig, filter_updt, ab_mag_orig, verbose=False):

		'''
		filter_orig: string
		path to original filter transmission data

		filter_updt: string
		path to overlapping filter transmission data

		ab_mag_orig: float
		magnitude measured using original filter

		verbose: bool
		if true, prints detailed information about the conversion
		'''

		import numpy as np
		from scipy.integrate import simpson

		# Load the filter data
		wav1, filt1 = np.loadtxt(f'filters/{self.fmap[filter_orig].replace('/', '.')}.dat', unpack=True)
		wav2, filt2 = np.loadtxt(f'filters/{self.fmap[filter_updt].replace('/', '.')}.dat', unpack=True)


		# Identify the wavelength range the 2 filters share in common
		wav_low = np.max([np.min(wav1), np.min(wav2)])
		wav_upp = np.min([np.max(wav1), np.max(wav2)])
		if verbose: print('Wavelength range: %g to %g Angstroms' % ( wav_low, wav_upp ))

		# Restrict the filter data to the common shared wavelengths
		f1_wavs = np.where((wav1 > wav_low) & (wav1 < wav_upp))[0]
		f2_wavs = np.where((wav2 > wav_low) & (wav2 < wav_upp))[0]

		wav1, filt1 = wav1[f1_wavs], filt1[f1_wavs]
		wav2, filt2 = wav2[f2_wavs], filt2[f2_wavs]

		# Integrate filter transmission data to get transmission ratio
		# Simpson's rule integral takes arguments simpson(y, x)
		# We want f2/f1 since flux_f2 = f2/f1*flux_f1
		f1_intgrl = simpson(y=(wav1*filt1), x=wav1)
		f2_intgrl = simpson(y=(wav2*filt2), x=wav2)
		ratio = f1_intgrl/f2_intgrl
		if verbose: print('Flux ratio f2/f1: ', ratio)
		
		# Per Appendix A derivation in Emily paper
		ab_mag_new = ab_mag_orig + 2.5*np.log10(ratio)
		if verbose: print('New AB mag: ', ab_mag_new)

		return ab_mag_new
	
	def mag_orig_to_flux(self, mag_orig, sigma_mag_orig):

		# propagate uncertainty through mag_orig -> flux conversion	
		# sigma_flux = sqrt(flux**2 * (-1/2.5 * ln(10) * sigma_mag_orig)**2)

		flux = np.power(10, (mag_orig+48.6)/-2.5)
		variance_flux = flux**2*(-1/2.5*np.ln(10)*sigma_mag)**2
		sigma_flux = np.sqrt(variance_flux)
		return flux, sigma_flux
		
	def flux_to_mag_new(self, flux, sigma_flux):
		
		# propagate uncertainty through flux -> new_mag conversion
		# sigma_mag_new = sqrt([-2.5 * sigma_flux/(flux * ln(10))]^2)

		mag_new = -2.5*np.log10(flux)-48.6
		variance_mag_new = np.power(-2.5 * sigma_flux/(flux * np.ln(10)), 2)
		sigma_mag_new = np.sqrt(variance_mag_new)
		return mag_new, sigma_mag_new	


	# update_photometry needs to be automated, current implementation is bad, too user-error prone
	# 1. loop over all photometry for a given event
	# 2. convert EVERY SINGLE instrument+band combination into LSST/2MASS variants, as LSST g may not be the same as GTC+OSIRIS g when doing full transmission, not just filters (which may be similar, but instruments are not)
	# 3. uncertainties:
	#	a) if an observation has e_magnitude, propagate that appropriately
	# 	b) if an observation has e_upper_magnitude and e_lower_magnitude, 
	#	   propagate each and take the average
	#	c) if observation is an upper limit, set e_magnitude to 0 for
	#	   propagation, then set it to 5 mag for inference (large uncertainty)
	# 4. update the photometry dictionaries with the new observations. loop over# each old observation, replacing it with all the new observations
	# 5. for preparing PE, make sure to use EM_PE json parser to generate standardized representations of the data 

	def filter_overlap(self, filter_orig, filter_updt):

		# load each of the filters
		wav1, filt1 = np.loadtxt(f'filters/{self.fmap[filter_orig].replace('/', '.')}.dat', unpack=True)
		wav2, filt2 = np.loadtxt(f'filters/{self.fmap[filter_updt].replace('/', '.')}.dat', unpack=True)

		xmin = min(wav1.min(), wav2.min())
		xmax = max(wav1.max(), wav2.max())

		dx = 0.1*(xmax-xmin)
		xmin -= dx
		xmax += dx
		# number of interpolated wavelength bins
		n_intp_wav_bins = int(1e3)
		x = np.linspace(xmin, xmax, n_intp_wav_bins)

		spl1 = np.interp(x, wav1, filt1, left=0, right=0)
		spl2 = np.interp(x, wav2, filt2, left=0, right=0)

		# where do we get at least 1% transmission from each filter?
		idx1 = spl1 > 0.01
		idx2 = spl2 > 0.01
		idx = np.logical_and(idx1, idx2)
		# if there are more than 20% of wavelength bins overlapping, assume overlapping
		if idx.sum() > int(0.20*n_intp_wav_bins):
			return filter_updt
		else: return None


	def update_photometry(self, convert_from_vega=False, verbose=False): 
		'''
		write me
		'''

		## Each N added observations will shift the old observation indices by N-1
		## (the -1 is from removing the old observations), so we add a counter
		## We assume the counter starts at 1 because, until we remove an observation,
		## all new observations should be added AFTER the initial, original observation
		obs_idx_offset = 1

		### TODO: HAVE THIS FUNCTION IDENTIFY THE OBSERVATIONS ON ITS OWN AND HANDLE E_MAGNITUDE AS IN ADJUST_FILTERS FUNCTION

		# dictionary keys are ordered, hooray!
		n_original_obs = len(self.photometry)

		# loop through each observation in the original photometry list
		for obs_idx in np.arange(n_original_obs):

			## do not redistribute converted fluxes, as dictionary will update in real-time
			#if 'converted' in observation['source']: continue
			# check with which grizyJHK filters original observation overlaps
					
			# store original observation data
			original_obs = self.photometry[obs_idx+obs_idx_offset-1]
			if "upperlimit" in original_obs.keys(): continue
			old_filt = self.get_filter_key(original_obs)
			old_mag = float(original_obs['magnitude'])
	
			# get the filter key as used in get_filters.py
			# identify which simulation filters overlap in wavelength space with original filter
			overlap_filters = [self.filter_overlap(old_filt, new_filt) for new_filt in self.sim_filters]
			# remove simulation filters which do not overlap from overlap list
			overlap_filters = [filt for filt in overlap_filters if filt is not None]
			if verbose: print(old_filt, overlap_filters)

			# if there is no overlap with out filters, just scrap the observation
			if len(overlap_filters) == 0:
				self.photometry = np.delete(self.photometry, obs_idx+obs_idx_offset-1).tolist()
				obs_idx_offset -= 1
				continue

			# loop through overlapping filters and redistribute flux
			for filt_idx in range(len(overlap_filters)):
				# in the case of the first new filter, remove old photometry
				if filt_idx == 0:
					# remove original observation from photometry list
					self.photometry = np.delete(self.photometry, obs_idx+obs_idx_offset-1).tolist()
					# decrement obs_idx_offset to account for removed observation
					obs_idx_offset -= 1

				# gather observation + filter data for flux redistribution

				new_filt = overlap_filters[filt_idx]
				new_mag = self.redistribute_flux(old_filt, new_filt, old_mag, verbose=False)
			
				# apply Vega offset if applicable
				if convert_from_vega: mag_new += self.vega_offsets[new_filt]

				new_obs_dict = original_obs.copy()
				new_obs_dict["magnitude"] = str(round(new_mag, 1))
				new_obs_dict["band"] = new_filt[-1]
				new_obs_dict["instrument"] = original_obs["instrument"]
				new_obs_dict["telescope"] = original_obs["telescope"]
				new_obs_dict["system"] = "AB"
				new_obs_dict["source"] = f"converted from {old_filt.split('.')[-1]}-band observation"
				if "e_magnitude" in original_obs.keys():
					new_obs_dict["e_magnitude"] = original_obs["e_magnitude"]
				elif ("e_upper_magnitude" in original_obs.keys() and \
				      "e_lower_magnitude" in original_obs.keys()):
					new_obs_dict["e_magnitude"] = str(np.mean([float(original_obs["e_lower_magnitude"]), float(original_obs["e_upper_magnitude"])]))
				#elif original_obs["upperlimit"] == True:
				#	new_obs_dict["e_magnitude"] = str(5)
				self.photometry = np.insert(self.photometry, obs_idx+obs_idx_offset, new_obs_dict).tolist()
				obs_idx_offset += 1

		print('Number original observations: ', n_original_obs, 'Number new observations: ', len(self.photometry))		

		self.jsondata[self.name]['photometry'] = self.photometry

		from pathlib import Path
		Path(f'{self.name}_data').mkdir(parents=True, exist_ok=True)

		with open(f'{self.name}_data/{self.name}.json', 'w') as f:
			json.dump(self.jsondata, f, ensure_ascii=True, indent=4)

if __name__=="__main__":

	import argparse
	
	parser = argparse.ArgumentParser()
	parser.add_argument('GRBpath', type=str, help='Path to GRB json file')
	args = parser.parse_args()

	# Print out original observation sources (telescopes/instruments)
	#thisGRB = GRB(args.GRBpath)
	#obs_sources = thisGRB.get_obs_sources()
	#print('Original observation sources')
	#print(obs_sources)
	#print('---')

	# Redistribute flux from original observations into new filters
	
	thisGRB = GRB(args.GRBpath)
	thisGRB.update_photometry()	
