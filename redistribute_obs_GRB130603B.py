import json
import numpy as np
import utils

times = []
f1s = []
f2s = []
old_band = []
new_band = []
old_obs = []
obs_idxs = []
instruments = []
telescopes = []
delete_flags = []

## V-band at t = 56446.66718981
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([56446.66718981, 56446.66718981])
f1s.extend(['v_SWIFT_UVOT.dat', 'v_SWIFT_UVOT.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([16.957, 16.957])
obs_idxs.extend([0, 0])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## V-band at t = 56446.74818981
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([56446.74818981, 56446.74818981])
f1s.extend(['v_SWIFT_UVOT.dat', 'v_SWIFT_UVOT.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([18.377, 18.377])
obs_idxs.extend([1, 1])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## V-band at t = 56446.93918981
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([56446.93918981, 56446.93918981])
f1s.extend(['v_Johnson_CAHA.dat', 'v_Johnson_CAHA.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([21.60, 21.60])
obs_idxs.extend([5, 5])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## F606W-band at t = 56456.02918981
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([56456.02918981, 56456.02918981, 56456.02918981])
f1s.extend(['f606w_HST_ACS.dat', 'f606w_HST_ACS.dat', 'f606w_HST_ACS.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([26.52, 26.52, 26.52])
obs_idxs.extend([32, 32, 32])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F160W-band at t = 56456.06918981
## F160W-band overlaps with H-band (see Figure 4 in reference)
## Reference: https://sites.astro.caltech.edu/~george/ay122/Bessel2005ARAA43p293.pdf

times.extend([56456.06918981])
f1s.extend(['f160w_HST_WFC3.dat'])
f2s.extend(['H_2MASS.dat'])
old_band.extend(["F160W"])
new_band.extend(["H"])
old_obs.extend([25.82])
obs_idxs.extend([33])
instruments.extend(["2MASS"])
telescopes.extend(["2MASS"])
delete_flags.extend([True])

## F160W-band at t = 56476.22918981
## F160W-band overlaps with H-band (see Figure 4 in reference)
## Reference: https://ui.adsabs.harvard.edu/abs/2005ARA%26A..43..293B/abstract

times.extend([56476.22918981])
f1s.extend(['f160w_HST_WFC3.dat'])
f2s.extend(['H_2MASS.dat'])
old_band.extend(["F160W"])
new_band.extend(["H"])
old_obs.extend([25.21])
obs_idxs.extend([37])
instruments.extend(["2MASS"])
telescopes.extend(["2MASS"])
delete_flags.extend([True])

utils.update_photometry('kne-parsed/GRB130603B.json', times, f1s, f2s, old_obs, obs_idxs, new_band, old_band, instruments, telescopes, delete_flags, convert_from_vega=False)

