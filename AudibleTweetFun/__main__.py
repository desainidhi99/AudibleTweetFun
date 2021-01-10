import sys
from ExtractTweets import *
from make_call import make_call

def main():
    '''
    Try-except to handle invalid or non-existing twitter account - TBD
    '''
    try:
        userID = input("Enter a Twitter handle: ")
        api_to_use = twitter_setup()
        result = tweet_extract(api_to_use, userID)
        print(result)

        # make_call(result)
    except tweepy.TweepError:
        print("This user does not exist!")

    ### number parameter for make_call function
    ### link main function 





if __name__ == '__main__':
    main()