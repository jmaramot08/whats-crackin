# Tracking cashtags that are currently trending on r/WallStreetBets using pushshift.io API

# This module pulls data from the r/WallStreetBets subreddit using pushshift.io
# and the PSAW Python Pushshift API wrapper, processes and outputs the top 10 cashtags
# to be displayed on the GUI.

from psaw import PushshiftAPI
import datetime as dt
from datetime import date

def retrieve_data():
    api = PushshiftAPI()
  
    today = date.today()

    month = int(today.strftime("%m"))
    day = int(today.strftime("%d"))
    year = int(today.strftime("%Y"))

    start_time = int(dt.datetime(year, month, day).timestamp())

    # grabs first "limit" submissions from given date (start_time), remove
    # after arg to grab latest "limit" submissions
    submissions = api.search_submissions(after=start_time,
                                subreddit='wallstreetbets',
                                filter=['url','author', 'title', 'subreddit'])
                                # limit=500) #delete to remove limit
     

    # dict to store cashtag keys and number of mentions as values
    cashtag_dict = {}

    # list to store each instance (mention) of a cashtag
    cashtags_list = []

    # populates cashtag_list with each cashtag mentioned
    for submission in submissions:
        words = submission.title.split()

        # inline function to filter out cashtags
        cashtags = list(set(filter(lambda word: word.lower().startswith('$') and word[1:].isalpha() and len(word) <=5, words)))
        
        if len(cashtags) > 0:
            cashtags_list.extend(cashtags)

    # fill cashtag_dict with cashtags and counts each time it is mentioned
    for cashtag in cashtags_list:
        if cashtag.upper() in cashtag_dict:
            cashtag_dict[cashtag.upper()] += 1
        else:
            cashtag_dict[cashtag.upper()] = 1

    # sort dict by number of mentions, grabs only top 10 items
    sorted_dict = dict(sorted(cashtag_dict.items(), key=lambda x: x[1], reverse=True)[:10])

    return sorted_dict