import tweepy
import sys
import re
from credentials import *

# authorization tokens
# Keys to be entered
from tweepy import TweepError

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

    for tweet in tweets[:5]:
        # tweet.full_text.encode('ascii', 'ignore').decode('ascii')
        five_recent_tweets.append(tweet.full_text)

    output = ""
    # for i in five_recent_tweets:
    #     if len(five_recent_tweets) >= 1:
    #         i = re.sub(r'http\S+', '', i, flags=re.MULTILINE)
    #         output += i + " "
    #     else:
    #         output = "This user has not posted any tweets"
    #
    # return output.encode('utf-8')

    if len(five_recent_tweets) >= 1:
        for i in five_recent_tweets:
            i.strip()
            i = re.sub(r'http\S+', '', i, flags=re.MULTILINE)
            output += i + ""
            output = output.replace('\n\n', '\n')
    else:
        output = "This user has not posted any tweets."

    return output.encode('utf-8')

    # if len(five_recent_tweets) >= 1:
    #     return "\n".join(five_recent_tweets)
    # # if twitter profile is empty
    # else:
    #     return "This user has not posted any tweets"


def main():
    '''
    Try-except to handle invalid or non-existing twitter account - TBD
    '''
    # try:
    #     userID = raw_input("Enter a Twitter handle: ")
    # except tweepy.TweepError as err:
    #     print(err)

    userID = raw_input("Enter a Twitter handle: ")
    api_to_use = twitter_setup()
    result = tweet_extract(api_to_use, userID)
    # print("\n".join(result))
    print(result)
    print(type(result))

if __name__ == "__main__":
    main()
