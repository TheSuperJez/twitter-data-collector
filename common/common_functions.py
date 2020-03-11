import os
import yaml

PATHS = {"in": "./data/followers/",
         "out": "./data/following/",
         "track": "./data/tracks",
         "names": "./data/screen_names/",
         "outputs": "./data/outputs/"}

def create_paths():
  path = PATHS.get("in")
  if not os.path.exists(path):
      os.makedirs(path)
  
  path = PATHS.get("track")
  if not os.path.exists(path):
      os.makedirs(path)

  path = PATHS.get("out")
  if not os.path.exists(path):
      os.makedirs(path)

  path = PATHS.get("names")
  if not os.path.exists(path):
      os.makedirs(path)

  path = PATHS.get("outputs")
  if not os.path.exists(path):
      os.makedirs(path)

def get_path(pathname):
  return PATHS.get(pathname)

def get_config():
  with open('./config.yml', 'r') as f:
    doc = yaml.load(f, Loader=yaml.FullLoader)
    config = {}
    config['CONSUMER_KEY'] = doc["CONSUMER_KEY"]
    config['CONSUMER_SECRET'] = doc["CONSUMER_SECRET"]
    config['ACCESS_TOKEN'] = doc["ACCESS_TOKEN"]
    config['ACCESS_TOKEN_SECRET'] = doc["ACCESS_TOKEN_SECRET"]
    return config