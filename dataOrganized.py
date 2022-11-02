#need to load file differently to do if statement for photometry separately
import glob
import json
filepath1 = glob.glob("/home/emily.monclus/kne-archival-pe/kne-2000-2029/*")
filepath2 = glob.glob("/home/emily.monclus/kne-archival-pe/kne-internal/GRB*")

def systemCounts(filepath):
	for file in filepath:
		print(file)
		list = file.split("/")
		last = list[-1]
		if last == "LICENSE":
			print("end")
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
					print(dictionary)
					for key in dictionary:
						if key == "system":
							if dictionary[key] == "Vega":
								print("Vega")
								vegacount += 1
								print(f"Vega count: {vegacount}")
							elif dictionary[key] == "AB":
								print("AB")
								abcount += 1
								print(f"AB count: {abcount}")
							else: # dictionary[key] != "Vega" and dictionary[key] != "AB":
								print("Other")
								othercount += 1
								print("System not Ab/Vega, system name:")
								print(dictionary[key])
						else:
							print("not system")
							
			print(f"Data end. Vegacount: {vegacount}. AB count: {abcount}. Other count: {othercount}.")

#systemCounts(filepath1)
systemCounts(filepath2)

