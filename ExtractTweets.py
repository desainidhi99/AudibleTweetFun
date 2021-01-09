import tweepy
from credentials import *

# authorization tokens
# Keys to be entered
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


def twitter_setup():
    # Twitter credentials authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


def tweet_extract(api, username):
    # initialize list of tweet
    five_recent_tweets = []

    tweets = api.user_timeline(screen_name=username, count=10, include_rts=False, tweet_mode='extended')
    
    # Extract the first 5 recent tweets
    for tweet in tweets[:5]:
        five_recent_tweets.append(tweet)
    
    # return the 5 tweets as a list
    return five_recent_tweets


def main():
    userID = raw_input("Enter a Twitter handle: ")
    api_to_use = twitter_setup()
    tweet_extract(api_to_use, userID)

if __name__ == "__main__":
    main()
