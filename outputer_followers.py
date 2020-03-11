from common import common_functions
from common import output_functions
import argparse
import tweepy
import os
import csv

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", required=True, help="Screen name of twitter user")
    args = vars(parser.parse_args())
    config = common_functions.get_config()
    auth = tweepy.OAuthHandler(config.get("CONSUMER_KEY"), config.get("CONSUMER_SECRET"))
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, retry_delay=60)

    user = args['user']
    ego = api.get_user(user).id   

    with open(os.path.join(common_functions.get_path("in"), str(ego)), 'r') as f:
        ego_neighbours = [int(id) for line in csv.reader(f) for id in line]
    output_functions.make_adjacency_matrix(ego_neighbours, direction = "in", file= user + '_in.csv')
    print("neighbours: ")
    print(ego_neighbours)
    print("\n")
    for i, userid in enumerate(ego_neighbours):
        try:
            with open(os.path.join(common_functions.get_path("in"), str(userid)), 'r') as f:
                print("Looking for: " + str(userid))
                sub_neighbours = [int(id) for line in csv.reader(f) for id in line]
            output_functions.make_adjacency_matrix(sub_neighbours, direction = "in", file= user + '_in.csv')
        except Exception as e:
            print(e)
            print("Skipping...")