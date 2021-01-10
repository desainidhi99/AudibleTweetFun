import tweepy
import sys
import re
from credentials import *
from make_call import make_call

# authorization tokens
# Keys to be entered
from tweepy import TweepError

consumer_key = "fjUEUMRNAhnCJ4sMwsO1s1Cok"
consumer_secret = "wglUybYJdmOKZWzruWSYhKQ959RBxlIf6ugxl6WcrEnqE73NTr"
access_token = "1121303268-Ba7Sp3kt39Y1qP5698h1igNFBvcASHAMltb4Agf"
access_token_secret = "C0YISCnKC4OGxvosXvek8pg5Mptf2CXR3GVckIa0pgqx4"

'''
This function sets up the Twitter access 
return the api
'''
def twitter_setup():
    # Twitter credentials authorization
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api

'''
This function extracts the tweets given inputs: api and username.
We extract only the tweets appear on the user's profile (no retweets, no replies).
Resulting tweets are cleaned and organized as a String for the twilio function.
'''
def tweet_extract(api, username):
    # initialize list of tweet
    five_recent_tweets = []

    # exclude retweets, exclude replies
    tweets = api.user_timeline(screen_name=username, count=200, include_rts=False, exclude_replies=True, tweet_mode='extended')
    
    #extract the first 5 recent tweets
    for tweet in tweets[:5]:
        five_recent_tweets.append(tweet.full_text)

    output = ""
    
    # for list greater than or equal 1
    if len(five_recent_tweets) >= 1:
        place_holder = 1
        for i in five_recent_tweets:
            # strip whitespaces
            i.strip()
            # remove hyperlinks "http"
            i = re.sub(r'http\S+', '', i, flags=re.MULTILINE)
            # if the tweet is empty bc it is only an image, tell user the tweet is only an image, add to output
            if i == "":
                output += "Tweet #" + str(place_holder) + ": " + "There is an image" + "."
            # else, if the tweet has text, add to output
            else:
                output += "Tweet #" + str(place_holder) + ": " + i + "."
            # remove any empty sentences
            output = output.replace('\n\n', '\n')
            place_holder += 1
    
    # if list is empty, print statement
    else:
        output = "This user has not posted any tweets."

    return output #.encode('utf-8')

def main():
    
if __name__ == "__main__":
    main()
