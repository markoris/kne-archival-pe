from astroquery.svo_fps import SvoFps
import numpy as np

fmap = {
	# Original observation filters
	'DanishR': 'LaSilla/DFOSC.Bessel_R',
	'Gemini-Nr': 'Gemini/GMOS-N.r',
	'HSTF814W': 'HST/ACS_WFC.F814W',
	'VLTI': 'Paranal/FORS2.ESO1077',
	'VLTR': 'Paranal/FORS2.ESO1076',
	'VLTV': 'Paranal/FORS2.ESO1075',
	'HST+ACSF606W': 'HST/ACS_WFC.F606W',
	'HST+ACSF814W': 'HST/ACS_WFC.F814W',
	'HST+WFPC2F606W': 'HST/WFPC2-WF.F606W',
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

for key in fmap.keys():
	fname = 'filters/'+fmap[key].replace('/', '.')+'.dat'
	print(fname)
	data = SvoFps.get_transmission_data(fmap[key])
	data = np.array([data['Wavelength'], data['Transmission']]).T
	np.savetxt(fname, data)

