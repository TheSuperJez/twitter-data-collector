from common import common_functions
import os
import csv

def make_adjacency_matrix(users,  direction="out", file = "adjacency.csv"):
	# Dictionary of usernames - id
	usernames = {}

	if(type(users[0]) == str):
		for uid in os.listdir(common_functions.get_path("names")):
			uid = int(uid)
			fname = os.path.join(common_functions.get_path("names"), str(uid))
			with open(fname, 'r') as f:
				uname = f.readline()
				if uname in users:
					usernames[uid]  = uname
	else:
		for uid in os.listdir(common_functions.get_path("names")):
			uid = int(uid)
			fname = os.path.join(common_functions.get_path("names"), str(uid))
			if uid in users:
				with open(fname, 'r') as f:
					uname = f.readline()
					usernames[uid]  = uname


	# Create a dictionary with neighbours of each user
	neighbours = {}
	
	for i, uid in enumerate(usernames):
		print("Processing: " + str(uid))
		fname = os.path.join(common_functions.get_path(direction), str(uid))
		try:
			with open(fname, 'r') as f:
				neighbours[uid] = [int(id) for line in csv.reader(f) for id in line]
			print(usernames[uid], direction, len(neighbours[uid]))
		except FileNotFoundError as e:
			print(e)
			print("WARNING: Cannot create the full adjacency because some neighbourhoods are missing")
			pass

	# Compute adjacency matrix and write into file
	with open(os.path.join(common_functions.get_path("outputs"), file), 'a+') as fout:
		csvwriter = csv.writer(fout, delimiter=',')
		for n in neighbours:
			for nn in neighbours[n]:	
				if(nn in usernames):
					if(direction == "out"):
						csvwriter.writerow([usernames[n], usernames[nn]])
					else:
						print("Relationship: " + usernames[nn] + " : " + usernames[n])
						csvwriter.writerow([usernames[nn], usernames[n]])