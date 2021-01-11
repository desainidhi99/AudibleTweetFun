# Audible Tweet Fun using Twilio and TwitterApi right on the Cell phone# !
## Overview

### Project Summary
Tell us the Twitter Handle and this app will play the most recent five Tweets for you on the registered cell# !.  

App is making use of [Tweepy Library](https://www.tweepy.org/) to access the Twitter Api. Calls are perfomed using [Twilio API](https://www.twilio.com/docs/libraries/python).
Complete app is written in Python Language.

### Authors
-  Spencer Griffin [Devpost ID](https://devpost.com/sgriffin10) ||  [sgri@seas.upenn.edu](sgri@seas.upenn.edu) ||  [Github](https://github.com/sgriffin10/)
-  Nidhi Desai [Devpost ID](https://devpost.com/desainidhi99) ||  [nidhide@seas.upenn.edu](nidhide@seas.upenn.edu) ||  [Github](https://github.com/desainidhi99/)
-  Gilbert Lau [Devpost ID](https://devpost.com/laugilpc) ||  [laugilpc@seas.upenn.edu](laugilpc@seas.upenn.edu) ||  [Github](https://github.com/laugil627/)

### Usage
  Please check the deployment section below to use the app and get ready to hear some tweets !
  
### Deployment
 #### PreRequisites :-
1. Need to install [Python](https://www.python.org/downloads/)
2. Need to install Tweepy Library using command 
```
pip install tweepy
```
3. Sign up for free [Twilio Account](https://www.twilio.com/login) to use desired cell# 
4. Verify the cell# with Twilio

#### Installation :-
1. Download the github repository on your local machine using below command
```
git clone https://github.com/desainidhi99/AudibleTweetFun
```
2. Change the API token values inside the ExtractTweets.py based on the values you have. You can get Access Tokens From [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access)
3. For Windows Users -> Open the Github Bash window and Navigate to the folder location where the file was saved on your local machine
- Console window takes input as follows:-
 ```
 1st Argument -> Twitter handle whose tweet you want to hear. Example - ElonMusk
 2nd Argument -> registered cell#
 ```
 - Finally you should get call and listen to your favourite user Tweets !
 
 ### Tools used
 What all tech stack did we use in our project ?
 - [Twilio](https://www.twilio.com/docs/libraries/python) It is an API to send and receive SMS, MMS, OTT messages globally and it is Secure.
 - [Tweepy](https://www.tweepy.org/) It is a Python library for accessing the Twitter API
 
 ### Test Cases covered
- User with less than 5 tweets will be handled
- Invalid user handle will result in error message
- User handle is NOT case sensitive
- Filters out images and web links for the Tweets. It lets user know that there is an Image inside the tweet.
 
 ### Future can look like
 - User has the option to register for the app using their cell# directly
 - Schedule the call either on desired time of day or whenever the new tweet appears 
 - We welcome any suggestions/comments for enhancement !!





