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

## SWIFT white band at t = 54589.51976602
## SWIFT white band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([54589.51976602, 54589.51976602, 54589.51976602])
f1s.extend(['white_SWIFT.dat', 'white_SWIFT.dat', 'white_SWIFT.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["white", "white", "white"])
new_band.extend(["g", "r", "i"])
old_obs.extend([20, 20, 20])
obs_idxs.extend([0, 0, 0])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## B-band at t = 54589.56945602
## B-band overlaps with g-band (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([54589.56945602])
f1s.extend(['B_KECK.dat'])
f2s.extend(['g_LSST.dat'])
old_band.extend(["B"])
new_band.extend(["g"])
old_obs.extend([26.00])
obs_idxs.extend([3])
instruments.extend(["LSSTCam"])
telescopes.extend(["LSST"])
delete_flags.extend([True])

## F450W-band at t = 54594.87653602
## F450W-band overlaps with g-band (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([54594.87653602])
f1s.extend(['f450w_HST_WFPC2.dat'])
f2s.extend(['g_LSST.dat'])
old_band.extend(["F450W"])
new_band.extend(["g"])
old_obs.extend([26.9])
obs_idxs.extend([15])
instruments.extend(["LSSTCam"])
telescopes.extend(["LSST"])
delete_flags.extend([True])

## F606W-band at t = 54594.87653602
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([54594.87653602, 54594.87653602, 54594.87653602])
f1s.extend(['f606w_HST_WFPC2.dat', 'f606w_HST_WFPC2.dat', 'f606w_HST_WFPC2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([27.01, 27.01, 27.01])
obs_idxs.extend([16, 16, 16])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F814W-band at t = 54594.87653602
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([54594.87653602, 54594.87653602, 54594.87653602])
f1s.extend(['f814w_HST_WFPC2.dat', 'f814w_HST_WFPC2.dat', 'f814w_HST_WFPC2.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([26.8, 26.8, 26.8])
obs_idxs.extend([17, 17, 17])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F606W-band at t = 54598.64737602
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([54598.64737602, 54598.64737602, 54598.64737602])
f1s.extend(['f606w_HST_WFPC2.dat', 'f606w_HST_WFPC2.dat', 'f606w_HST_WFPC2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([28.0, 28.0, 28.0])
obs_idxs.extend([18, 18, 18])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F814W-band at t = 54598.64737602
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([54598.64737602, 54598.64737602, 54598.64737602])
f1s.extend(['f814w_HST_WFPC2.dat', 'f814w_HST_WFPC2.dat', 'f814w_HST_WFPC2.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([27.1, 27.1, 27.1])
obs_idxs.extend([19, 19, 19])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

utils.update_photometry('kne-parsed/GRB080503.json', times, f1s, f2s, old_obs, obs_idxs, new_band, old_band, instruments, telescopes, delete_flags, convert_from_vega=False)

