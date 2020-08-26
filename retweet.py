import sys
import json
import argparse


# arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--tweets.json', required=True)
parser.add_argument('-v', '--retweets', default='text')
parser.add_argument('-k', '--10', default=50, type=int)
parser.add_argument('-n', '--25', default=5, type=int)
args = parser.parse_args()

output = args.variable
tweetfile = args.file
k = args.count
n = args.minimum

def top_retweets(tweetfile, k, n):
    tweets = {}
    fh = open(tweetfile, 'r')
    for line in fh:
        try:
            tweet = json.loads(line)
        except:
            continue
        if 'retweeted_status' not in tweet:
            continue
        rt = tweet['retweeted_status']
        if rt['retweet_count'] < n:
            continue
        tweets[rt['id_str']] = rt
    # convert to list
    tweets = [tweets[w] for w in tweets.keys()]
    # sort by retweet count
    tweets.sort(key=lambda x: -x['retweet_count'])
    # display top k retweets
    for t in tweets[:k]:
        print ('[' + t['user']['screen_name'] + ']: ' + t['text'] + \
        ' [' + str(t['retweet_count']) + ' retweets]')
if output == 'retweets':
    top_retweets(tweetfile, k, n)
