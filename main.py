import tweepy
import twitterColorDetection

#Get keys and split them into their variables

#Put keys in file called twitterkeys.txt with each on a new line
#consumer_key first, consumer_secret second
#access_token third, access_token_secret fourth

f = open("twitterkeys.txt","r")
keys = f.read()
keys = keys.split("\n")

consumer_key = keys[0]
consumer_secret = keys[1]
access_token = keys[2]
access_token_secret = keys[3]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Only tweet if the tower is not white
###Disabled for the first night as a test.  Uncomment loop and tab the line after to enable

if (colorDetection.outText != "The tower is white today!"):

    #api.update_with_media("out.jpg", colorDetection.outText)

    #For Sugarbowl: If UT wins tweet with special message!

    messageText = "Orange Tower Celebrates Big 12 Title"
    api.update_with_media("out.jpg", messageText)