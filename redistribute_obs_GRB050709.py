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

## V-band at t = 53563.40546
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53563.40546, 53563.40546])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([24.45, 24.45])
obs_idxs.extend([3, 3])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## V-band at t = 53565.30616
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53565.30616, 53565.30616])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([25.1, 25.1])
obs_idxs.extend([5, 5])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## F814W-band at t = 53566.65610
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53566.65610, 53566.65610, 53566.65610])
f1s.extend(['f814w_HST_ACS.dat', 'f814w_HST_ACS.dat', 'f814w_HST_ACS.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([24.66, 24.66, 24.66])
obs_idxs.extend([7, 7, 7])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F814W-band at t = 53570.78585
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53570.78585, 53570.78585, 53570.78585])
f1s.extend(['f814w_HST_ACS.dat', 'f814w_HST_ACS.dat', 'f814w_HST_ACS.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([25.39, 25.39, 25.39])
obs_idxs.extend([10, 10, 10])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## V-band at t = 53571.42768
## V-band overlaps with g- and r-bands (see Fig 2.3 in reference)
## Reference: http://www.eso.org/sci/facilities/paranal/instruments/fors/doc/VLT-MAN-ESO-13100-1543_P110.2.pdf

times.extend([53571.42768, 53571.42768])
f1s.extend(['v_FORS2.dat', 'v_FORS2.dat'])
f2s.extend(['g_LSST.dat', 'r_LSST.dat'])
old_band.extend(["V", "V"])
new_band.extend(["g", "r"])
old_obs.extend([24.5, 24.5])
obs_idxs.extend([12, 12])
instruments.extend(["LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST"])
delete_flags.extend([True, False])

## F814W-band at t = 53579.64469
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53579.64469, 53579.64469, 53579.64469])
f1s.extend(['f814w_HST_ACS.dat', 'f814w_HST_ACS.dat', 'f814w_HST_ACS.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([27.16, 27.16, 27.16])
obs_idxs.extend([13, 13, 13])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

## F814W-band at t = 53595.63756
## F814W-band overlaps with i-, z- and y-bands (see bottom figure in reference)
## Reference: https://www.lsst.org/sites/default/files/img/lsst_ideal_filter_curve_jan_2008.png

times.extend([53595.63756, 53595.63756, 53595.63756])
f1s.extend(['f814w_HST_ACS.dat', 'f814w_HST_ACS.dat', 'f814w_HST_ACS.dat'])
f2s.extend(['i_LSST.dat', 'z_LSST.dat', 'y_LSST.dat'])
old_band.extend(["F814W", "F814W", "F814W"])
new_band.extend(["i", "z", "y"])
old_obs.extend([27.4, 27.4, 27.4])
obs_idxs.extend([14, 14, 14])
instruments.extend(["LSSTCam", "LSSTCam", "LSSTCam"])
telescopes.extend(["LSST", "LSST", "LSST"])
delete_flags.extend([True, False, False])

utils.update_photometry('kne-parsed/GRB050709.json', times, f1s, f2s, old_obs, obs_idxs, new_band, old_band, instruments, telescopes, delete_flags, convert_from_vega=True)

