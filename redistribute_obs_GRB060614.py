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

## V-band at t = 53902.25075667
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53902.25075667, 53902.25075667])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([21.38, 21.38])
obs_idxs.extend([0, 0])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## V-band at t = 53903.36556667
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53903.36556667, 53903.36556667])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([22.88, 22.88])
obs_idxs.extend([4, 4])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## V-band at t = 53904.39118667
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53904.39118667, 53904.39118667])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([23.64, 23.64])
obs_idxs.extend([8, 8])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## V-band at t = 53908.35831667
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53908.35831667, 53908.35831667])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([24.85, 24.85])
obs_idxs.extend([12, 12])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## F814W-band at t = 53914.10169667
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53914.10169667, 53914.10169667, 53914.10169667])
f1s.extend(['f814w_HST_WFPC2.dat', 'f814w_HST_WFPC2.dat', 'f814w_HST_WFPC2.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([24.77, 24.77, 24.77])
obs_idxs.extend([15, 15, 15])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F606W-band at t = 53914.50064667
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53914.50064667, 53914.50064667, 53914.50064667])
f1s.extend(['f606w_HST_WFPC2.dat', 'f606w_HST_WFPC2.dat', 'f606w_HST_WFPC2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([26.25, 26.25, 26.25])
obs_idxs.extend([16, 16, 16])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## V-band at t = 53924.33005667
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53924.33005667, 53924.33005667])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([24.8, 24.8])
obs_idxs.extend([19, 19])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## F814W-band at t = 53931.62896667
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53931.62896667, 53931.62896667, 53931.62896667])
f1s.extend(['f814w_HST_ACS.dat', 'f814w_HST_ACS.dat', 'f814w_HST_ACS.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([27.3, 27.3, 27.3])
obs_idxs.extend([22, 22, 22])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F606W-band at t = 53932.29715667
## F606W-band overlaps with g-, r-, and i-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53932.29715667, 53932.29715667, 53932.29715667])
f1s.extend(['f606w_HST_ACS.dat', 'f606w_HST_ACS.dat', 'f606w_HST_ACS.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat', 'i_LSST.dat'])
old_band.extend(["F606W", "F606W", "F606W"])
new_band.extend(["g", "r", "i"])
old_obs.extend([27.9, 27.9, 27.9])
obs_idxs.extend([23, 23, 23])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F814W-band at t = 53945.48682667
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53945.48682667, 53945.48682667, 53945.48682667])
f1s.extend(['f814w_HST_ACS.dat', 'f814w_HST_ACS.dat', 'f814w_HST_ACS.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([27.4, 27.4, 27.4])
obs_idxs.extend([26, 26, 26])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

utils.update_photometry('kne-parsed/GRB060614.json', times, f1s, f2s, old_obs, obs_idxs, new_band, old_band, instruments, telescopes, delete_flags, convert_from_vega=False)

