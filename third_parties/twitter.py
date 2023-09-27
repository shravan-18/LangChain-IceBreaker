import os
from datetime import timezone, datetime
import logging
from decouple import Config

import tweepy

# Create a Config object
config = Config(
    "D:\VIT Material\VIT material\Courses\Langchain\Github\ice_breaker\.env"
)

logger = logging.getLogger("twitter")

auth = tweepy.OAuthHandler(
    config.get("TWITTER_API_KEY"), config.get("TWITTER_API_SECRET")
)

auth.set_access_token(
    config.get("TWITTER_ACCESS_TOKEN"), config.get("TWITTER_ACCESS_SECRET")
)

api = tweepy.API(auth)


def scrape_user_tweets(username, num_tweets=5):
    """
    Scrapes a Twitter user's original tweets (ie., not retweets or replies) and returns them as a list of dictionaries.
    Each dictionary has three fields: "time_posted" (relative to now), "text" and "url".
    """

    tweets = api.user_timeline(screen_name=username, count=num_tweets)

    tweet_list = []

    for tweet in tweets:
        if "RT @" not in tweet.text and not tweet.text.startswith("@"):
            tweet_dict = {}
            tweet_dict["time_posted"] = str(
                datetime.now(timezone.utc) - tweet.created_at
            )
            tweet_dict["text"] = tweet.text
            tweet_dict[
                "url"
            ] = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
            tweet_list.append(tweet_dict)

        return tweet_list
