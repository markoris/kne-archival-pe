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

## F160W-band at t = 57064.3
## F160W-band overlaps with H-band (see Figure 4 in reference)
## Reference: https://ui.adsabs.harvard.edu/abs/2005ARA%26A..43..293B/abstract

times.extend([57064.3])
f1s.extend(['f160w_HST_WFC3.dat'])
f2s.extend(['H_2MASS.dat'])
old_band.extend(["F160W"])
new_band.extend(["H"])
old_obs.extend([25.1])
obs_idxs.extend([4])
instruments.extend(["2MASS"])
telescopes.extend(["2MASS"])
delete_flags.extend([True])

## F606W-band at t = 56456.02918981
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([57064.3])
f1s.extend(['f606w_HST_WFC3.dat', 'f606w_HST_WFC3.dat', 'f606w_HST_WFC3.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([25.6, 25.6, 25.6])
obs_idxs.extend([5, 5, 5])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

utils.update_photometry('kne-parsed/GRB150101B.json', times, f1s, f2s, old_obs, obs_idxs, new_band, old_band, instruments, telescopes, delete_flags, convert_from_vega=False)

