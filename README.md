# Audible Tweet Fun using Twilio and TwiiterApi right on the Cell phone# !
## Overview

### Project Summary
Tell us the Twitter Handle and this app will play the most recent five Tweets for you on the registered cell# !.  

App is making use of [Tweepy Library](https://www.tweepy.org/) to access the Twitter Api. Calls are perfomed using [Twilio API](https://www.twilio.com/docs/libraries/python).
Complete app is written in Python Language.

### Authors
-  Spencer Griffin [Devpost ID]() [Github](https://github.com/sgriffin10/)
-  Nidhi Desai [Devpost ID](https://devpost.com/desainidhi99) [Github](https://github.com/desainidhi99/)
-  Gilbert Lau [Devpost ID](https://devpost.com/laugilpc) [Github](https://github.com/laugil627/)

### Usage
  Please check the deployment section below to use the app and get ready to hear some tweets !
  
### Deployment
 #### PreRequisites :-
1. Need to install Python, Tweepy 
2. Need to have regsitered Phone number with Twilio account. (Default account limits only 3 verified numbers that can be used)
- You can Fork these project directly from your Github account or  Download the project from below location :-
- For Windows Users -> Open the Github Bash window and Navigate to the folder location where the file was saved on your local machine and enter arguments as below :
- Console window takes input as follows:-
 ```
 1st Argument -> user handle
 2nd Argument -> registered cell#
 ```
 ### Tools used
 What all tech stack did we use in our project ?
 - [Twilio](https://www.twilio.com/docs/libraries/python) It is an API to send and receive SMS, MMS, OTT messages globally and it is Secure.
 - [Tweepy](https://www.tweepy.org/) It is a Python library for accessing the Twitter API
 
 ### Test Cases covered
- User with less than 5 tweets will be handled
- Invalid user handle will result in error message
- Filters out images and web links. It lets user know that there is an Image inside the tweet
 
 ### Future can look like
 - User has the option to register for the app using their cell#
 - Schedule the call either on desired time of day or whenever the new tweet appears 
 - We welcome any suggestions/comments for enhancement !!





