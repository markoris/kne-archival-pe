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
	# GRB 050709 -> not being used! remove after rest of obs done, just example for now
	'DanishR': 'LaSilla/DFOSC.Bessel_R',
	'Gemini-Nr': 'Gemini/GMOS-N.r',
	'HSTF814W': 'HST/ACS_WFC.F814W',
	'VLTI': 'Paranal/FORS2.ESO1077',
	'VLTR': 'Paranal/FORS2.ESO1076',
	'VLTV': 'Paranal/FORS2.ESO1075',
	'HST+ACSF606W': 'HST/ACS_WFC.F606W',
	'HST+ACSF814W': 'HST/ACS_WFC.F814W',
	'HST+WFPC2F606W': 'HST/WFPC2-WF.F606W',
	# GRB130603B
	'CAHAV' 
	'GTCr' 
	'Gemini-Northg' 
	'Gemini-Northi' 
	'Gemini-Northr'
	'Gemini-Northz'
	'Gemini-Southg' 
	'Gemini-Southi' 
	'Gemini-Southr'
	'HSTF160W' 
	'HSTF606W' 
	'MMTr' 
	'Magellan/Baader' 
	'Magellan/Clayr' 
	'NOTr'
	'SwiftV' 
	'TNGi' 
	'TNGr' 
	'UKIRTJ' 
	'UKIRTK' 
	'VLTJ' 
	'WHTg' 
	'WHTi' 
	'WHTz'
	# GRB150101B
	'Geminir'
	'HSTF160W'
	'HSTF606W'
	'Magellanr'
	'VLTJ'
	# GRB160821B
	'GTCg'
	'GTCi'
	'GTCr'
	'GTCz'
	'HSTF110W'
	'HSTF160W'
	'HSTF606W' 
	'KeckIKs'
	# GRB211211A
	#'DOTU: 'Generic/Bessell.U',
	#'DOTV: 'Generic/Bessell.V',
	#'KMTNet/SSOR': 'Generic/Johnson.R',
	#'KMTNet/SAAOI': 'Generic/Johnson.I',
	# etc...
	# Destination filters
	'lsstg': 'LSST/LSST.g',
	'lsstr': 'LSST/LSST.r',
	'lssti': 'LSST/LSST.i',
	'lsstz': 'LSST/LSST.z',
	'lssty': 'LSST/LSST.y',
	'2massj': '2MASS/2MASS.J',
	'2massh': '2MASS/2MASS.H',
	'2massk': '2MASS/2MASS.Ks'
}

# DOT filters not recorded on SVO Filter Profile Service
# Use generic Bessel scaled by transmission values from 
# Kumar+ (2022) JApA...43...27K
DOT_transmissions = {'DOTU': 0.49,
		     'DOTB': 0.62,
		     'DOTV': 0.80,
		     'DOTR': 0.79,
		     'DOTI': 0.80}

# B/V 0.85, R 0.90, I 0.80

KMTNet_transmissions = {'KMTNet/SSOR': 0.90,
			'KMTNet/SAAOR': 0.90,
			'KMTNet/CTIOR': 0.90 
			'KMTNet/SSOI': 0.80,
			'KMTNet/SAAOI': 0.80,
			'KMTNet/CTIOI': 0.80,
			}	

for key in fmap.keys():
	fname = 'filters/'+fmap[key].replace('/', '.')+'.dat'
	print(fname)
	data = SvoFps.get_transmission_data(fmap[key])
	data = np.array([data['Wavelength'], data['Transmission']]).T
	# For instruments with no transmission data, use generic filters
	# and scale by reported transmission, if applicable
	if 'DOT' in key: data[:, 1] *= DOT_transmissions[key]
	if 'KMTNet' in key: data[:, 1] *= KMTNet_transmissions[key]
	np.savetxt(fname, data)

