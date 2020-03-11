# Twitter Data Collector
It is a Python3 project for collecting, transforming and applying analitics on Twitter data.

# Current state
At this first develop phase, it only collects data from:
- A keyword query
- Followers from user (2 levels as BFS)
And outputs an adjacency mtrix from followers.

# Install Deps
```
pip3 install -r requiremients.txt
```
# Collect data from keword query
```
python3 collector_tracker.py -k "#MyHashTag"
```
it will create an output on data/tracks/#MyHashTag.json with all the collected tweets, this file needs to be fixed adding a [ at the begining of the file and a ] at the end of file.


# Collect data from keword query
```
python3 collector_tracker.py -k "#MyHashTag"
```

It will create an output on data/tracks/{keyword}.json with all the collected tweets, this file needs to be fixed adding a [ at the begining of the file and a ] at the end of file.

# Collect followers data from user
```
python3 collector_followers.py -u usersname
```
This will collect 2 levels of the follower's userID on data/followers/{userID} and the screen name on data/scree_names/{userID}

# Create adjacency matrix (on Development)
```
python3 outputer_followers.py -u username
```
This will create the adjacency matrix on data/output/{username}.csv

# TODO
- Documentation on files
- More outputers
- analytics