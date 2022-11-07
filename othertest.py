import glob, json
filepath1 = glob.glob("/home/emily.monclus/kne-archival-pe/kne-parsed/*")
def systemCounts(filepath):
	totalvega = 0
	totalab = 0
	totalother = 0
	for file in filepath:
		print(file)
		list = file.split("/")
		last = list[-1]
		if last[0:2] == "GW" or last[0:2] == "LI" or last[0:2] == "RE":
			print("GW/LI/RE")
		else:
			event = last[0:-5]
			print(f" Event: {event}")
			with open(file, "r") as read_file:
				data = json.load(read_file, encoding="UTF-8")
			eventdata = data[event]
			keys = eventdata.keys()
			if "photometry" not in keys:
				print("No photometry")
			else:
				vegacount = 0
				abcount = 0
				othercount = 0
				for dictionary in data[event]['photometry']:
					if "system" not in dictionary:
						othercount +=1
					for key in dictionary:
						if key == "system":
							if dictionary[key] == "Vega":
								vegacount += 1
								print(f"Vega count: {vegacount}")
							elif dictionary[key] == "AB":
								abcount += 1
								print(f"AB count: {abcount}")
							else:
								othercount += 1
								print("System not Ab/Vega, system name:")
				totalother += othercount
				totalvega += vegacount
				totalab += abcount
			print(f"File end. Vegacount: {vegacount}. AB count: {abcount}. Other count: {othercount}.")
			print(totalother," ", totalvega," ", totalab)

systemCounts(filepath1)

