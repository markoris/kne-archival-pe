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

## F606W-band at t = 57625.564
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([57625.564, 57625.564, 57625.564])
f1s.extend(['f606w_HST_WFC3.dat', 'f606w_HST_WFC3.dat', 'f606w_HST_WFC3.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([26.02, 26.02, 26.02])
obs_idxs.extend([8, 8, 8])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F160W-band at t = 57625.631
## F160W-band overlaps with H-band (see Figure 4 in reference)
## Reference: https://ui.adsabs.harvard.edu/abs/2005ARA%26A..43..293B/abstract

times.extend([57625.631])
f1s.extend(['f160w_HST_WFC3.dat'])
f2s.extend(['H_2MASS.dat'])
old_band.extend(["F160W"])
new_band.extend(["H"])
old_obs.extend([24.53])
obs_idxs.extend([9])
instruments.extend(["2MASS"])
telescopes.extend(["2MASS"])
delete_flags.extend([True])

## F110W-band at t = 57625.697
## F110W-band overlaps with J-band (see Figure 4 in reference)
## Reference: https://ui.adsabs.harvard.edu/abs/2005ARA%26A..43..293B/abstract

times.extend([57625.697])
f1s.extend(['f110w_HST_WFC3.dat'])
f2s.extend(['J_2MASS.dat'])
old_band.extend(["F110W"])
new_band.extend(["J"])
old_obs.extend([24.82])
obs_idxs.extend([10])
instruments.extend(["2MASS"])
telescopes.extend(["2MASS"])
delete_flags.extend([True])

## F606W-band at t = 57632.325
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([57632.325, 57632.325, 57632.325])
f1s.extend(['f606w_HST_WFC3.dat', 'f606w_HST_WFC3.dat', 'f606w_HST_WFC3.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([27.9, 27.9, 27.9])
obs_idxs.extend([11, 11, 11])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F110W-band at t = 57645.108
## F110W-band overlaps with J-band (see Figure 4 in reference)
## Reference: https://ui.adsabs.harvard.edu/abs/2005ARA%26A..43..293B/abstract

times.extend([57645.108])
f1s.extend(['f110w_HST_WFC3.dat'])
f2s.extend(['J_2MASS.dat'])
old_band.extend(["F110W"])
new_band.extend(["J"])
old_obs.extend([26.9])
obs_idxs.extend([12])
instruments.extend(["2MASS"])
telescopes.extend(["2MASS"])
delete_flags.extend([True])

## F160W-band at t = 57632.449
## F160W-band overlaps with H-band (see Figure 4 in reference)
## Reference: https://ui.adsabs.harvard.edu/abs/2005ARA%26A..43..293B/abstract

times.extend([57632.449])
f1s.extend(['f160w_HST_WFC3.dat'])
f2s.extend(['H_2MASS.dat'])
old_band.extend(["F160W"])
new_band.extend(["H"])
old_obs.extend([26.6])
obs_idxs.extend([13])
instruments.extend(["2MASS"])
telescopes.extend(["2MASS"])
delete_flags.extend([True])

utils.update_photometry('kne-parsed/GRB160821B.json', times, f1s, f2s, old_obs, obs_idxs, new_band, old_band, instruments, telescopes, delete_flags, convert_from_vega=False)

