def systemCounts(directory, verbose=True):
	"""
	This is called a docstring. It briefly describes the purpose of the code,
	as well as the datatypes and structure of the inputs.

	This script analyzes the magnitude systems reported for GRB observations.
	Magnitude systems other than AB or Vega are classified as "other".
	Observations which have no reported magnitude system are classified as "other".

	directory: str
		   Path to directory containing .json files containing GRB observational data
		   as formatted in astrocats (github.com/astrocatalogs)

	verbose:   bool
		   Boolean (true/false) operator which determines whether results
		   are printed to standard output (the terminal)
	"""

	# load our module dependencies within the function that uses them, not in the main program
	import glob
	import json

	# assume our user points us to the directory, so we collect all the files in there
	filepath = glob.glob(directory+'/*')
	# define our total counts for the population of GRB observations
	counts_total = {"Vega": 0, "AB": 0, "other": 0}
	# we want to omit using "file" as it is a protected variable
	for f in filepath:
		# define our counts per event
		counts = {"Vega": 0, "AB": 0, "other": 0}
		# get the filename to use as a dictionary key
		fname = f.split('/')[-1][:-5]
		# get photometry directly, do not save the opened file as we will not be using it
		photometry = json.load(open(f), encoding="UTF-8")[fname]['photometry']
		# let's loop through our observations in a fancy Pythonic way
		# we want to loop through each observation in the event's photometry
		# if "system" is one of the keys in the observation, record what it is
		# otherwise, if "system" is not in the observation keys, assume it is "other"
		# return the list of magnitude systems to the mag_systems variable
		mag_systems = [observation["system"] if "system" in observation.keys() else "other" for observation in photometry]
		# now update our counts, both per-event and population, after looping through the
		# event's photometry
		for system in mag_systems:
			counts[system] += 1 
			counts_total[system] += 1
		# print per-event counts at the end of the loop, but still within the loop
		# only prints the output if the user specifies the "verbose" option
		if verbose: print("Counts for %s: " % fname, counts)
	# print the total counts outside of the loop, after all events have been analyzed
	# only prints the output if the user specifies the "verbose" option
	if verbose: print("Counts for all events: ", counts_total)

# if this is the main program being executed, then do the lines below
if __name__ == "__main__":
	# run the function systemCounts on the kne-parsed directory
	# since we are running the script from the same directory in which the kne-parsed directory
	# exists, we don't have to specify a full filepath, just a local one
	systemCounts('kne-parsed', verbose=True)

