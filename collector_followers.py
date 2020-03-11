import argparse
import tweepy
from tweepy import TweepError
from followers import followers
from common import common_functions
import time

DIRECTION = "in" #Followers

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", required=True, help="Screen name of twitter user")
    parser.add_argument("--force", type=bool, required=False, help="Forces re-fetching of users")
    api_data = common_functions.get_config()
    common_functions.create_paths()
    args = vars(parser.parse_args())
    user = args['user']
    force = args['force']

    while(True): 
        try:
            followers.get_neighbourhood_bfs(api_data, user, DIRECTION, force = force)            
            break
        except TweepError as e:
            print(e)
            time.sleep(60)
