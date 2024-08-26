from astroquery.svo_fps import SvoFps
import numpy as np

# The necessary filters are obtained by supplying the 
# GRBXXXXXX.json file to utils.get_obs_sources(path_to_json).

# As the process requires mapping the correct telescope, 
# instrument, and filter information to the appropriate SVO ID, 
# the mapping of the .json data to the SVO ID was done manually.
# The mapping of all relevant filters is presented below.
 
fmap = {
	# Original observation filters
	# GRB130603B
	'CAHA.DLR-MKIII.V': 'Generic/Johnson.V',  ### GENERIC
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
	'NOT.MOSCA.r': None, ### Obtained NOT.MOSCA.r Gunn r filter from https://www.not.iac.es/instruments/filters/filters.php
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
	'DOT.IMAGER.B': 'Generic/Bessell.B',
	'DOT.IMAGER.I': 'Generic/Bessell.I',
	'DOT.IMAGER.R': 'Generic/Bessell.R',
	'DOT.IMAGER.U': 'Generic/Bessell.U',
	'DOT.IMAGER.V': 'Generic/Bessell.V',
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
	'CTIO.KMTNet.I': 'Generic/Johnson.I', 	### Generic
	'CTIO.KMTNet.R': 'Generic/Johnson.R', 	### Generic
	'ElSauce.RASA36.R' : 'Generic/Johnson.R', ### Generic
	'Gemini.GMOS-S.r': 'Gemini/GMOS-S.r',
	'Gemini.GMOS-S.z': 'Gemini/GMOS-S.z',
	'SAAO.KMTNet.I': 'Generic/Johnson.I', 	### Generic
	'SAAO.KMTNet.R': 'Generic/Johnson.R',
	'SAAO.PRIME.H': '2MASS/2MASS.H', ### Calibrated to 2MASS per Yang 2024 Nature paper 
	'SAAO.PRIME.J': '2MASS/2MASS.J', ### Calibrated to 2MASS per Yang 2024 Nature paper
	'SAAO.PRIME.Y': 'Paranal/VISTA.Y_filter', ### Calibrate to VISTA per Yang 2024 Nature paper
	"SOAR.GHTS.z'": 'TNO/ULTRACAM.z-3', ### Could not find exact match, using close substitute 
	'SSO.KMTNet.I': 'Generic/Johnson.I', 	### Generic
	'SSO.KMTNet.R': 'Generic/Johnson.R', 	### Generic
	'Swift.UVOT.u': 'Swift/UVOT.U_fil',
	'Swift.UVOT.white': 'Swift/UVOT.white_fil',
	'TESS.TESS.Red': 'TESS/TESS.Red',
	'VLT.XSH.K': 'Paranal/HAWKI.Ks', # Use HAWK-I Ks band as proxy, no Xshooter filter data
	# Destination filters
	'LSST.LSST.g': 'LSST/LSST.g',
	'LSST.LSST.r': 'LSST/LSST.r',
	'LSST.LSST.i': 'LSST/LSST.i',
	'LSST.LSST.z': 'LSST/LSST.z',
	'LSST.LSST.y': 'LSST/LSST.y',
	'2MASS.2MASS.J': '2MASS/2MASS.J',
	'2MASS.2MASS.H': '2MASS/2MASS.H',
	'2MASS.2MASS.Ks': '2MASS/2MASS.Ks'
}

# DOT filters not recorded on SVO Filter Profile Service
# Use generic Bessel scaled by transmission values from 
# Kumar+ (2022) JApA...43...27K
DOT_transmissions = {'DOT.IMAGER.U': 0.49,
		     'DOT.IMAGER.B': 0.62,
		     'DOT.IMAGER.V': 0.80,
		     'DOT.IMAGER.R': 0.79,
		     'DOT.IMAGER.I': 0.80}

# B/V 0.85, R 0.90, I 0.80

KMTNet_transmissions = {'SSO.KMTNet.R': 0.90,
			'SAAO.KMTNet.R': 0.90,
			'CTIO.KMTNet.R': 0.90, 
			'SSO.KMTNet.I': 0.80,
			'SAAO.KMTNet.I': 0.80,
			'CTIO.KMTNet.I': 0.80,
			}	

for key in fmap.keys():
	if 'NOT.MOSCA' in key or 'Generic' in fmap[key]:
		fname = 'filters/'+key.replace('/', '.')+'.dat'
	else:
		fname = 'filters/'+fmap[key].replace('/', '.')+'.dat'
	print(fname)
	if 'NOT.MOSCA' in key:
		import requests
		url = "https://www.not.iac.es/instruments/filters/curves-ascii/14.txt"
		data = requests.get(url).content
		with open(fname, "wb") as file:
			file.write(data)
		data = np.loadtxt(fname)
		data[data[:, 1] < 0, 1] = 0
		data[:, 1] /= 100
		data[:, 0] *= 10
		np.savetxt(fname, data)
		continue
	data = SvoFps.get_transmission_data(fmap[key])
	data = np.array([data['Wavelength'], data['Transmission']]).T
	# For instruments with no transmission data, use generic filters
	# and scale by reported transmission, if applicable
	if 'DOT' in key: data[:, 1] *= DOT_transmissions[key]
	if 'KMTNet' in key: data[:, 1] *= KMTNet_transmissions[key]
	np.savetxt(fname, data)

