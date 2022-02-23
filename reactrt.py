import tweepy
import time, os
from dotenv import load_dotenv
config = load_dotenv()
conf = os.getenv("TWITTER_API")

print(conf)