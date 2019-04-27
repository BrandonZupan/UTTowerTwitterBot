import tweepy
import twitterColorDetection
import requests
import bs4
from PIL import Image

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

towerColorRGB = twitterColorDetection.getRGB()
towerColor = twitterColorDetection.getColorNames(towerColorRGB[0], towerColorRGB[1])
#towerColor = "yeet"

#Check to see if the color is tweet worthy
print(towerColor)

if (towerColor[0] and towerColor[1] == "White"):
    raise Exception("Tower color is not worthy of a tweet")

else:
    #Attempt to get the color from UT's website and assemble a message
    url = 'https://tower.utexas.edu/'
    print(url)
    try:
        res = requests.get(url)
        #Make sure the website isn't borked
        res.raise_for_status()
        #print(websiteStatus)

        #Find the element and make the tweet text whatever UT says it is
        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        titleContainer = soup.findAll("section", {"class": "widget custom_widget_recent_entries"}) 
        #print(titleContainer)
        title = titleContainer[0].getText()
        titleList = title.split()
        tweetText = ' '.join(titleList[3:-3])
        #print("Message: " + tweetText)
    except:
        #To do, create tweetText and make it work, also make it tweet color if the default message is on website
        print('yeet')

    #Get image
    im = Image.open('tower.jpg')
    tweetImage = twitterColorDetection.createImage(502,73,930,478, im)

    #api.update_with_media(tweetImage, tweetText)
    print(tweetText)

"""
#Only tweet if the tower is not white
###Disabled for the first night as a test.  Uncomment loop and tab the line after to enable

if (colorDetection.outText != "The tower is white today!"):

    #api.update_with_media("out.jpg", colorDetection.outText)

    #For Sugarbowl: If UT wins tweet with special message!

    messageText = "Orange Tower Celebrates Big 12 Title"
    api.update_with_media("out.jpg", messageText)
"""