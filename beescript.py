#importing random crap
import tweepy
from time import sleep
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY'] #cause y'all shouldn't know it
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#opens up the stupid script whatevr
my_file=open('fakebeescript.txt','r')
file_lines=my_file.readlines()
my_file.close()

for line in file_lines:
# Add try ... except block to catch and output errors
    try:
        print(line)
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(3600)