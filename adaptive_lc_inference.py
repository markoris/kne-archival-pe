import numpy as np
import corner
import torch
import torch.nn as nn
import os, sys
os.environ["OMP_NUM_THREADS"] = "20"
sys.path.append('/home/marko.ristic/RIT-matters/communications/20230901-YingleiMarko-AutoencoderPE/Kilonova-Neural-Network')
import matplotlib.pyplot as plt
from KilonovaInterpolator import VAE, Encoder, Decoder, DataProcessor
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('data_dir')
parser.add_argument('bands')
parser.add_argument('distance')
parser.add_argument('nmax')
args = parser.parse_args()

# Define function to calculate distance (in time) weighted magnitude
def time_weighted_magnitude(m_low, m_upp, t_low, t_upp, t_ref):
	m_weighted = ((t_upp - t_ref) * m_low + (t_ref - t_low) * m_upp) / (t_upp - t_low)
	return m_weighted	

### Loading light-curve times, saved VAE models for each band,
### and observational data for each band 

# Establish working bands
#bands = 'grizyJHK'
bands = args.bands

# Get VAE and times from Yinglei's git repo

cwd = os.getcwd()
os.chdir('Kilonova-Neural-Network')

times = np.load('times.npy')

nns = {'g': torch.load('AE_g_real_angle_logm.pt'),
	'r': torch.load('AE_r_real_angle_logm.pt'),
	'i': torch.load('AE_i_real_angle_logm.pt'),
	'z': torch.load('AE_z_real_angle_logm.pt'),
	'y': torch.load('AE_y_real_angle_logm.pt'),
	'J': torch.load('AE_J_real_angle_logm.pt'),
	'H': torch.load('AE_H_real_angle_logm.pt'),
	'K': torch.load('AE_K_real_angle_logm.pt'),
	}

os.chdir(cwd)

# Load data from EM_PE format for consistency

data = {}
for band in args.bands:
	data[band] = np.loadtxt(args.data_dir+f'/{band}.dat')

### Create random draws of n_samples samples

# Set limits for input spaces
# md, vd, mw, vw

param_mins = [-3, 0.05, -3, 0.05, 0]
param_maxs = [-1, 0.30, -1, 0.30, 90] # 165-180 is the same angular bin 

# Generate samples


# Residual is zero to start for all samples

def evaluate_logL(*samples_raw, distance=''):

        samples = DataProcessor().to_torch_tensor(samples_raw)[0]
        samples = samples.T

        residual = np.zeros_like(samples[:, 0])

### Loop through bands to calculate residual

        for band in bands:
		# reshape for good behavior with single observations
                data[band] = data[band].reshape(-1, 4)
                # Get observation times for specified band
                obs_times = data[band][:, 0]
                obs_mags = data[band][:, 2]
                obs_sigma = data[band][:, 3]
                # Find the upper-bound time indices 
                time_indices_upper = np.array([np.searchsorted(times, obs_times[t], 'right') for t in range(len(obs_times))])
                times_upper = times[time_indices_upper]
                # Upper bounds are just one index lower
                time_indices_lower = time_indices_upper-1
                times_lower = times[time_indices_lower]
	### Evaluate VAE for 1e8 samples to retrieve 1e8 light curves of size 264
                nns[band].eval()
                with torch.no_grad():
                        prediction, _, _ = nns[band](samples)
                prediction = prediction.numpy()
	# Get 1e8 lower mags and 1e8 upper mags
                mags_lower = prediction[:, time_indices_lower]
                mags_upper = prediction[:, time_indices_upper]
	# Calculate time-weighted magnitude for each sample
                mags_weighted = time_weighted_magnitude(mags_lower, mags_upper, times_lower, times_upper, obs_times)
	# Add distance modulus factor of distance in Mpc to source
                mags_weighted += 5*np.log10(float(args.distance)*1e6)-5
	# Calculate residual (mags_weighted - band_obs)^2/(sigma_obs)^2
                sys_sigma = 1.0 # 1.0 mag uncertainty to account for magnitude conversions
                sigma = np.sqrt(obs_sigma**2 + sys_sigma**2)
                mags_residual = ((mags_weighted - obs_mags)/sigma)**2
	# Sum residuals mags_residual.sum(axis=0) to be left with 1e8 residuals, one for each sample
                mags_residual_sum = mags_residual.sum(axis=1)
                print('%s-band mean residual (normalized to num data): ' % band, mags_residual_sum.mean()/len(obs_times))
                #print(mags_residual_sum.shape)
	# Add individual band contribution to residual to overall residual value
                residual += mags_residual_sum
                #print('%s-band finished' % band)

        for i in range(samples.shape[1]):
                idx_bad = np.where((samples[:, i] > param_maxs[i]) | (samples[:, i] < param_mins[i]))[0]
                residual[idx_bad] = 1e4

#        residual -= residual.min()
        return -0.5*residual


from RIFT.integrators import mcsampler, mcsamplerEnsemble, mcsamplerGPU, mcsamplerAdaptiveVolume

sampler = mcsamplerAdaptiveVolume.MCSampler()

indx = 0
params =['log_md', 'vd', 'log_mw', 'vw', 'theta'] 
for name in params:
        llim = param_mins[indx]
        rlim = param_maxs[indx]
        dx = rlim - llim
        indx += 1  # move along
        if name == 'theta':
                from scipy.stats import norm
                prior = np.vectorize(lambda x, L=dx:norm.pdf(x, loc=0, scale=5)) # Gaussian centered at 0 degrees with sigma = 5 degrees
        else:
                prior = np.vectorize(lambda x,L=dx:1./L)
        sampler.add_parameter(name, np.vectorize(lambda x,L=dx:1./L), 
            #prior_pdf=np.vectorize(lambda x,L=dx:1./L),
            prior_pdf=prior,
            left_limit=llim, right_limit=rlim,
            adaptive_sampling=True)

integral, var, eff_samp, _ = sampler.integrate(evaluate_logL, distance=args.distance, *params,  nmax=int(float(args.nmax)), max_iter=2,min_iter=2, \
        no_protect_names=True, save_intg=True,verbose=True, tempering_exp=0.5, tempering_adapt=True, temper_log=True, use_lnL=True, return_lnI=True)

lnL = sampler._rvs["log_integrand"] 
lnL -= lnL.max() 
lnp = sampler._rvs["log_joint_prior"]  
lnps = sampler._rvs["log_joint_s_prior"]
    ### compute weights of samples
weights = np.exp(lnL + lnp - lnps )
weights /= weights.sum()
# np random choice on the  using the weights as probabilities
samples = np.zeros((int(eff_samp), 9))
for i in range(len(params)):
	param = sampler._rvs[params[i]]
	if i == 0: param_idxs = np.random.choice(np.arange(len(param)), size=int(eff_samp), p=weights/weights.sum()) 
	samples[:, i] = param[param_idxs]
samples[:, 5] = lnL[param_idxs]
samples[:, 6] = lnp[param_idxs]
samples[:, 7] = lnps[param_idxs]
samples[:, 8] = weights[param_idxs]

#samples[:, 1] = 10**samples[:, 1]
#samples[:, 3] = 10**samples[:, 3]

n_ess = np.sum(weights)**2/np.sum(weights**2)
print("AV  n_eff, n_ess ", eff_samp,n_ess)
np.savetxt(f'{args.data_dir}/samples.dat', samples)
