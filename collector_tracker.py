#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml

import argparse
from tracker import tracker
from common import common_functions


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword", required=True, help="Word or hashtag to track")
    args = vars(parser.parse_args())
    api_data = common_functions.get_config()
    common_functions.create_paths()
    keyword = args["keyword"]
    print("Twitter data collector will store the new tweets for " + keyword)
    input("Press Enter to continue...")
    tracker.track(api_data, common_functions.get_path("track"), keyword)
    
    print(args)
    


