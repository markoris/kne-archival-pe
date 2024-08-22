import json
import numpy as np

# March 7th, 2023 at 15:44:06.67 UTC to Modified Julian Date (MJD)
T0 = 2460011.155633 - 2400000.5

print(T0)

data = np.loadtxt('data_from_paper_tables/GRB230307A.dat', dtype=str)

# Remove upper limits, only keep direct observations
upper_limit_idxs = np.where(data[:, -1] == 'u.l.')[0]
data = np.delete(data, upper_limit_idxs, axis=0)

# Remove observations prior to 0.125 days, outside of our LC model grid
#time_limit_idxs = np.where((data[:, 0].astype('float') < 0.125), (data[:, 0].astype('float') > 8.35))[0]
time_limit_idxs = np.logical_or(data[:, 0].astype('float') < 0.125, data[:, 0].astype('float') > 8.35)
#time_limit_idxs = np.logical_or([(np.where(data[:, 0].astype('float') < 0.125)[0]), (np.where(data[:, 0].astype('float') > 8.35))])
data = np.delete(data, time_limit_idxs, axis=0)

print(data)

instruments = 	{
		'TESS': {
			'telescope': 'TESS',
			'instrument': 'TESS'},
		'RASA36': {
			'telescope': 'El Sauce',
			'instrument': 'RASA36'},
		'KMTNet/SSO': {
			'telescope': 'SSO',
			'instrument': 'KMTNet'},
		'KMTNet/SAAO': {
			'telescope': 'SAAO',
			'instrument': 'KMTNet'},
		'KMTNet/CTIO': {
			'telescope': 'CTIO',
			'instrument': 'KMTNet' },
		'UVOT': {
			'telescope': 'Swift',
			'instrument': 'UVOT'},
		'PRIME': {
			# 2MASS JH VISTA Y SkyMapper Z
			'telescope': 'SAAO',
			'instrument': 'PRIME'},
		'Gemini': {
			'telescope': 'Gemini',
			'instrument': 'GMOS-S'},
		'SOAR': {
			'telescope': 'SOAR',
			'instrument': 'GHTS'},
		'XSH': {
			'telescope': 'VLT',
			'instrument': 'XSH'}
		}
	

photometry = []

for obs in data:
	photometry.append(
			{
			"time": str(T0 + float(obs[0])),
			"band": str(obs[2].strip()),
			"instrument": instruments[obs[1].strip()]["instrument"],
			"telescope": instruments[obs[1].strip()]["telescope"],
			"magnitude": str(obs[3].strip()),
			"e_magnitude": str(obs[4].strip()),
			"source": "1",
			"u_time": "MJD",
			}
			)

grbdict = {"GRB230307A":
		{"schema":"https://github.com/astrocatalogs/supernovae/blob/d3ef5fc/SCHEMA.md",
		 "name": "GRB211211A",
		"sources":[
			{
				"name":"2024Natur.626..742Y",
				"bibcode":"2024Natur.626..742Y",
				"reference":"Yang et al. (2022)",
				"alias":"1"
			},
		],
		"redshift":[
			{
				"value":"0.0647",
				"source":"1"
			}
		],
		"photometry": photometry
		}
}

json_obj = json.dumps(grbdict, indent=8)
with open("kne-for-pe/GRB230307A.json", "w") as outfile:
	outfile.write(json_obj)
