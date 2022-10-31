#working on cleaning up print statements
import glob
import json
filepath = glob.glob("/home/emily.monclus/ArchiveData/kne-2000-2029/*")
filepath2 = glob.glob("/home/emily.monclus/ArchiveData/kne-internal/*")

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
				data = json.load(read_file, encoding="UTF-8")[event]['photometry']
			vegacount = 0
			abcount = 0
			othercount = 0
			for dictionary in data:
				print(dictionary)
				for key in dictionary:
					if key == "system":
						if dictionary[key] == "Vega":
							vegacount += 1
							print(f"Vega count: {vegacount}")
						elif dictionary[key] == "AB":
							abcount += 1
							print(f"AB count: {abcount}")
						elif dictionary[key] != "Vega" and dictionary[key] != "AB":
							othercount += 1
							print("System not Ab/Vega, system name:")
							print(dictionary[key])
					else: #make into elif for no system key
						print("")
	print(f"Data end. Vegacount: {vegacount}. AB count: {abcount}. Other count: {othercount}.")

systemCounts(filepath)
systemCounts(filepath2)

