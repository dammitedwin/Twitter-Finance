import tweepy
import configparser

#read config
config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['twitter']['consumer_key']
consumer_secret = config['twitter']['consumer_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']



auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth,wait_on_rate_limit=True)

