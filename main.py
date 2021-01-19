import tweepy
import datetime
import csv #Import csv
consumer_key = "##############################"
consumer_secret = "g#############################################"
access_token = "##############################################"
access_token_secret = "###########################################"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)
#Girlfriend's twitter account

username = input("Enter username:")
tweets = []
moTweets = []
#("@ferzcour" in tweet.text or "@redfercuco" in tweet.text):

startDate = datetime.datetime(2015, 7, 1)
endDate = datetime.datetime(2015, 12, 1)
def printTweets():
    # Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
    # foreach through all tweets pulled
    tmpTweets = api.user_timeline(username, count=20)

    while (tmpTweets[-1].created_at > startDate):
        print("Last Tweet @", tmpTweets[-1].created_at, " - fetching some more")
        tmpTweets = api.user_timeline(username, max_id=tmpTweets[-1].id)
        for tweet in tmpTweets:
            if endDate > tweet.created_at > startDate:
                if (not tweet.retweeted) and ('RT @' not in tweet.text):
                    tweets.append(tweet)
# Retrieves tweets from a timeline and writes them to file
def get_user_timeline_tweets():
    f = open(username + ".txt", "w")
    for tweet in tweepy.Cursor(api.user_timeline, id=username).items(3200):
        if (not tweet.retweeted) and ('RT @' not in tweet.text):
            tweets.append(tweet)
    for tweet in tweets:
        url = f"https://twitter.com/{username}/status/{tweet.id}"
        dt = tweet.created_at
        f.write(dt.strftime("%B %d, %Y") + " " + tweet.text + "[ " + url + " ]" '\n')
# Ranks users by # of likes (TODO: ...)
def rankPeople():
    people = []
    for x in range(0, 3):
        name = input("Enter a user: ")
        people.append(name)

get_user_timeline_tweets()
