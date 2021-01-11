import sys
from ExtractTweets import *
from make_call import make_call

def main():
    '''
    Try-except to handle invalid or non-existing twitter account - TBD
    '''
    #variable for while loop
    call_again = True

    #while user wants to receive another call, continue loop 
    while call_again == True:
        try:
            #takes twitter username input
            userID = input("Enter a Twitter handle: ")

            #takes receiving phone number input
            phone_number = input("Enter your 10 digit phone number (no spaces and no country code! eg. 6178458393): ")

            #sets up twitter api and extracts first 5 tweets
            api_to_use = twitter_setup()
            result = tweet_extract(api_to_use, userID)
            
            #debugging purposed
            print(result)
            stopper = input("")

            #makes call to phone number and reads first 5 tweets from desired twitter username
            make_call(result,phone_number)
        except tweepy.TweepError:
            print("This user does not exist!")

        #asks user if they want program to call and read out tweets from another twitter user
        call_again_input = input("Would you like to search up another user's tweets? ").lower()
        if call_again_input == "no":
            call_again = False
        else:
            continue

if __name__ == '__main__':
    main()