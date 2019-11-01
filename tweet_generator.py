from dotenv import load_dotenv
import tweepy, os

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






