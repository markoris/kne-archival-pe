#file used to test counting for "other" systems
import glob
import json
filepath1 = glob.glob("/home/emily.monclus/kne-archival-pe/kne-internal/*")

def systemCounts(filepath):
	for file in filepath:
		print(file)
		list = file.split("/")
		last = list[-1]
	#	if last == "LICENSE":
		#	print("end")
		if last[0:2] == "GW" or "LI":
			print("GW/LI")
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
					if "system" not in keys:
						print("no system in obs, othercount:")
						othercount += 1
						print(othercount)
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
							elif dictionary[key] != "Vega" and dictionary[key] != "AB":
								print("Other")
								othercount += 1
								print("System not Ab/Vega, system name:")
								print(dictionary[key])
						else:
							print(f"{key} not system")
							
			print(f"Data end. Vegacount: {vegacount}. AB count: {abcount}. Other count: {othercount}.")


systemCounts(filepath1)

