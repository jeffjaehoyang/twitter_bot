from dotenv import load_dotenv
import tweepy, os, pytz, datetime, time
from tzlocal import get_localzone

load_dotenv()

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET_KEY = os.getenv("CONSUMER_SECRET_KEY")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET_KEY = os.getenv("ACCESS_SECRET_KEY")

def tweet(status):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET_KEY)
    api = tweepy.API(auth)
    api.update_status(status)

    return status

def fetch_timestamp():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET_KEY)
    api = tweepy.API(auth)
    last_tweet = api.user_timeline(id = api.me().id, count = 1)[0]
    timestamp = last_tweet.created_at #returns datetime.datetime object
    local_timezone = get_localzone()
    smart_timestamp = timestamp.replace(tzinfo=pytz.utc).astimezone(local_timezone).strftime('%Y-%m-%d, %H:%M')
    
    return smart_timestamp





