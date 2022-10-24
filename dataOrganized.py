import glob
import json
filepath = glob.glob("/home/emily.monclus/ArchiveData/kne-2000-2029/*")
#filepath2 = glob.glob("/home/emily.monclus/ArchiveData/kne-internal/*")
for file in filepath:
	print(file)
	list = file.split("/")
	print(list)
	last = list[-1]
	print(f" Last: {last}")
	if last == "LICENSE":
		print("end")
	else:
		event = last[0:-5]
		print(f" Event: {event}")
		with open(file, "r") as read_file:
			data = json.load(read_file, encoding="UTF-8")[event]['photometry']
			print(data)
		vegacount = 0
		abcount = 0
		othercount = 0
		for dictionary in data:
			print("dictionary found")
			print(dictionary)
			for key in dictionary:
				print("key found")
				print(key)
				if key == "system":
					print("system key found")
					print(dictionary[key])
					if dictionary[key] == "Vega":
						#print(
						vegacount += 1
						print(vegacount)
					elif dictionary[key] == "AB":
						abcount += 1
						print(abcount)
					elif dictionary[key] != "Vega" and dictionary[key] != "AB":
						othercount += 1
						print("System not Ab/Vega, system name:")
						print(dictionary[key])
				else:
					print("Incorrect key")
print(f"Data end. Vegacount: {vegacount}. AB count: {abcount}. Other count: {othercount}.")



