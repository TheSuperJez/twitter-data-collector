from common import common_functions
from common import twitter_functions

import tweepy

def get_neighbourhood_bfs(api_data, ego_screenname, direction = "in", force = False):
    """ Get the neighbours of ego and the neighbours of its neighbours
        Store everyting in files
    """
    auth = tweepy.OAuthHandler(api_data.get("CONSUMER_KEY"), api_data.get("CONSUMER_SECRET"))
    auth.set_access_token(api_data.get("ACCESS_TOKEN"), api_data.get("ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    ego = api.get_user(ego_screenname).id
    neighbours = twitter_functions.api_neighbours_ids(ego, api, direction= direction)
    print(str(len(neighbours)) + " Followers from: " + str(ego))
    users = neighbours
    users.append(ego)
    print("Fetching names")
    print("\n")
    twitter_functions.screen_names(users, api)
    print("\n")
    print("End fetching names")
    print("Save neighbours")
    print(neighbours)
    common_functions.append_to_cursor(neighbours)

    filepath=open("data/cursor.txt", "r")
    # Let's get the second level
    for line_no, line in enumerate(filepath):
        print("\n")
        print("User: " + line)
        print("Count: " + str(line_no))
        sub_neighbours = twitter_functions.fetch_neighbours(line, api, direction = direction, force = force)
        common_functions.append_to_cursor(sub_neighbours)
    filepath.close()