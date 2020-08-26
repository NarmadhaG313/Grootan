import tweepy
import json
import csv
import pandas as pd

consumer_key = '6YN3ADq54iGvcGhyHhMyGTA5K'
consumer_secret = 'pNtlL3hu2SZx1QhOGr8ZDAN5G6zSq6HYyyoy16wbbuS2DuEPiy'
access_token = '1298566666972884994-H9PHGJY1x3qPrw1K3quSwzCfB1LUhC'
access_token_secret = 'GUrzGG5Nu9BHhkyQfwebx4wLOme1vjUHjEuS3tOfKhSD5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
csvFile = open('ua.csv', 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#Corona",count=10,
                           lang="en",
                           since="2021-08-21").items():
    print(tweet.created_at,tweet.user.screen_name)
    csvWriter.writerow([tweet.created_at,tweet.text.encode('utf-8')])
