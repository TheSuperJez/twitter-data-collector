from os import listdir
import os
import json

import argparse
import os
import csv
import tweepy
import datetime
import numpy as np
import yaml
import json
import time
from tweepy import TweepError
from matplotlib import pylab as plt
from collections import Counter
from common import common_functions

def screen_names(users, api):
	"""Get the screen name of users"""
	n_users = len(users) + 1
	batch_start = 0
	batch_end = min(100, n_users)
	while(batch_start < n_users):
		try:
			users_batch = api.lookup_users(users[batch_start:batch_end])
			for u in users_batch:
				print(u.screen_name, u.id)
				with open(os.path.join(common_functions.get_path("names"), str(u.id)), 'w') as f:
					f.write(u.screen_name)
		except TweepError as e:
			print(e)
			time.sleep(60)

		batch_start += 100
		batch_end = min(batch_end+100, n_users)

def fetch_neighbours(userid, api, direction="in", force=False):
	fname = os.path.join(common_functions.get_path(direction), str(userid))
	neighbours = []

	# If user is already tracked, get their followers from file
	if(not force):
		if os.path.isfile(fname):
			print("User had already been fetched")
			return neighbours

	# otherwise use the API
	try:
		with open(fname, 'w') as f:
			print("fetching neighbours")
			neighbours = api_neighbours_ids(userid, api, direction)
			print("Followers: " + str(len(neighbours)))
			csv.writer(f).writerow(neighbours)
			screen_names(neighbours, api)

	except TweepError as e:
		print(e)
		if e == "Not authorized.":
			csv.writer(f).writerow('')
	return neighbours

def api_neighbours_ids(user, api, direction="in"):
	if direction == "in":
		neighbours_ids = tweepy.Cursor(api.followers_ids, id=user, count=5000).items()
	else:
		neighbours_ids = tweepy.Cursor(api.friends_ids, id=user, count=5000).items()

	neighbours_ids = [n for n in neighbours_ids]
	return neighbours_ids