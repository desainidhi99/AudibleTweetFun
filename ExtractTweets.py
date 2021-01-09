import tweepy
from credentials import *

# authorization tokens
# Keys to be entered
consumer_key = "fjUEUMRNAhnCJ4sMwsO1s1Cok"
consumer_secret = "wglUybYJdmOKZWzruWSYhKQ959RBxlIf6ugxl6WcrEnqE73NTr"
access_token = "1121303268-Ba7Sp3kt39Y1qP5698h1igNFBvcASHAMltb4Agf"
access_token_secret = "C0YISCnKC4OGxvosXvek8pg5Mptf2CXR3GVckIa0pgqx4"


def twitter_setup():
    # Twitter credentials authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api


def tweet_extract(api, username):
    # initialize list of tweet
    five_recent_tweets = []

    # exclude retweets, exclude replies
    tweets = api.user_timeline(screen_name=username, count=200, include_rts=False, exclude_replies=True, tweet_mode='extended')

    # status = api.get_status(username)
    #
    # for i in status.text[:5]:
    #     five_recent_tweets.append(i)
    #
    # return five_recent_tweets

    for tweet in tweets[:5]:
        five_recent_tweets.append(tweet.full_text)

    if len(five_recent_tweets) >= 1:
        return "\n".join(five_recent_tweets)
    # if twitter profile is empty
    else:
        return "This user has not posted any tweets"


def main():
    userID = raw_input("Enter a Twitter handle: ")
    api_to_use = twitter_setup()
    result = tweet_extract(api_to_use, userID)
    # print("\n".join(result))
    print(result)

if __name__ == "__main__":
    main()
