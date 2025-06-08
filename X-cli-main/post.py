import os
import sys

import tweepy
from dotenv import load_dotenv

load_dotenv()


def post_tweet(tweet_text):
    client = tweepy.Client(
        bearer_token=os.environ["BEARER_TOKEN"],
        consumer_key=os.environ["API_KEY"],
        consumer_secret=os.environ["API_KEY_SECRET"],
        access_token=os.environ["ACCESS_TOKEN"],
        access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
    )

    client.create_tweet(text=tweet_text)  # noqa


if __name__ == "__main__":
    post_tweet(sys.argv[1])
