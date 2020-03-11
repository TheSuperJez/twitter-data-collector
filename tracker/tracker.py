import tweepy
import datetime
import codecs
import json

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        coordinates = status.coordinates
        epochs = (status.created_at - datetime.datetime(2020,1,1)).total_seconds()
        user = status.user.screen_name
        user_id = status.user.id
        user_location = status.user.location
        text = status.text
        print(text)
            
        fname = outputfile + '.json'
        with codecs.open(fname, "a", "utf-8") as f:
            data = {}
            data['user'] = user
            data['user_id'] = user_id
            data['user_location'] = user_location
            data['timestamp'] = epochs
            data['text'] = text
            data['coordinates'] = coordinates
            f.write(json.dumps(data, indent = 4, ensure_ascii=False))
            f.write(",")


def track(api_data, path, keyword):
    auth = tweepy.OAuthHandler(api_data.get("CONSUMER_KEY"), api_data.get("CONSUMER_SECRET"))
    auth.set_access_token(api_data.get("ACCESS_TOKEN"), api_data.get("ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    global outputfile
    outputfile = path + "/" + keyword
    myStream.filter(track=keyword)


