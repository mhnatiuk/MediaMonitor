import urllib
import json
import tweepy
import ipdb
from time import sleep
from time import time
from time import strftime
from pymongo import MongoClient

class MongoHandler:

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.twitter
        self.tweets = self.db.twitter.tweets
    def insert_json_list(self, json_list):
        number_of_inserted = sum([self.insert_json(json_obj) for json_obj in json_list ])
        return number_of_inserted
    def insert_json(self, json_obj):
        ipdb.set_trace()
        results = self.tweets.find( {'id_str' : json_obj.id_str})
        if results.count() > 0:
            return 0
        else:
            json_str = unicode(json_obj).strip()
            self.tweets.insert(json_str)
            return 1
        
def auth():
    # The consumer keys can be found on your application's Details
    # page located at https://dev.twitter.com/apps (under "OAuth settings")
    consumer_key="nXID1ORfZ0cS4FKehmCGDQ"
    consumer_secret="KJjh44S3j6MlYfySzWK8KHaHdERn0EbV9JQgS06WA"
    
    # The access tokens can be found on your applications's Details
    # page located at https://dev.twitter.com/apps (located 
    # under "Your access token")
    access_token="34597270-eurWtocS5LWvRZznZMg5F1zOM6Dn6xFom3lRdZKb8"
    access_token_secret="4znBQi06IYx7mxxw7mcIIyJKQdQGd3lO4yXOfV4GDo"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
    assert api.me()['name'] == "mikolajhnatiuk"
    
    # If the application settings are set for "Read and Write" then
    # this line should tweet out the message to your account's 
    # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
    
    return api



    
def get_recent_polish_tweets():
    api = auth()
    place_id = "d9074951d5976bdf" # Poland
    tweets = api.search(q="place:%s" % place_id, include_entities="true", count=200)
    return tweets

def get_max_tweet_id(tweets):
    max_id = max([int(tweet['id_str']) for tweet in tweets])
    assert max_id is not None and max_id > 0, "Ooops there were no tweets or something else is going on"
    return max_id
def log(number):
    fh = open("log.txt", "a")
    fh.write( strftime("%a, %d %b %Y %H:%M:%S +0000", time()) + ";" + str(number) + "\n")
    fh.close()

def save_tweets(tweets):
    mongo_hd = MongoHandler()
    number_of_inserted_tweets = mongo_hd.insert_json_list(tweets)
    log(number_if_inserted_tweets)
    print "Number of inserted tweets %s" % number_of_inserted_tweets
    
if __name__ == '__main__':
    tweets = get_recent_polish_tweets()
    highest_tweet_id = get_max_tweet_id(tweets)
    save_tweets(tweets)
    



