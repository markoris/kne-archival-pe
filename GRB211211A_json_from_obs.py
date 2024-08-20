import json
import numpy as np

# December 11, 2021 at 13:59:09.0 UTC to Modified Julian Date (MJD)
T0 = 2459560.082743 - 2400000.5

data = np.loadtxt('data_from_paper_tables/GRB211211A.dat', dtype=str)

# Remove upper limits, only keep direct observations
upper_limit_idxs = np.where(data[:, -1] == 'u.l.')[0]
data = np.delete(data, upper_limit_idxs, axis=0)

# Remove observations prior to 0.125 days, outside of our LC model grid
time_limit_idxs = data[:, 0].astype('float') < 0.125
data = np.delete(data, time_limit_idxs, axis=0)

print(data)

instruments = 	{
		'DOT': {
			'telescope': 'DOT',
			'instrument': 'IMAGER',
			},
		'MITSUME': {
			'telescope': 'OAO',
			'instrument': 'MITSUME'},
		'UVOT': {
			'telescope': 'Swift',
			'instrument': 'UVOT'},
		'CAHA': {
			'telescope': 'CAHA',
			# CAHA instrument unclear, used g'r'i' filters
			# no record of instrument/telescope details, assuming
			# LAICA as sdss g'r'i' are close to sdss gri on LAICA
			# and that will give an actual instrument response
			'instrument': 'LAICA?' },
		'Gemini': {
			'telescope': 'Gemini',
			'instrument': 'GMOS-S'},
		'MMT': {
			'telescope': 'MMT',
			'instrument': 'MMIRS'}
		}
	

photometry = []

for obs in data:
	photometry.append(
			{
			"time": str(T0 + float(obs[0])),
			"band": str(obs[3].strip()),
			"instrument": instruments[obs[2].strip()]["instrument"],
			"telescope": instruments[obs[2].strip()]["telescope"],
			"magnitude": str(obs[4].strip()),
			"e_magnitude": str(obs[5].strip()),
			"source": "1",
			"u_time": "MJD",
			}
			)

grbdict = {"GRB211211A":
		{"schema":"https://github.com/astrocatalogs/supernovae/blob/d3ef5fc/SCHEMA.md",
		 "name": "GRB211211A",
		"sources":[
			{
				"name":"2022Natur.612..228T",
				"bibcode":"2022Natur.612..228T",
				"reference":"Troja et al. (2022)",
				"alias":"1"
			},
			{
				"name":"2023Univ....9..245T",
				"bibcode":"2023Univ....9..245T",
				"reference":"Troja (2023)",
				"alias":"2"
			}
		],
		"redshift":[
			{
				"value":"0.0785",
				"source":"2"
			}
		],
		"photometry": photometry
		}
}

json_obj = json.dumps(grbdict, indent=8)
with open("kne-for-pe/GRB211211A.json", "w") as outfile:
	outfile.write(json_obj)
