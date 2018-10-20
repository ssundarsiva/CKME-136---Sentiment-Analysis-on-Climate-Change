
# coding: utf-8

# In[32]:


import tweepy
from tweepy import OAuthHandler


consumer_key = 'tpnWWaY7Ctlr4DwgR3gIANzRm'
consumer_secret = 'inW2Ju0iC0FdQmZHhvU8RH8QvjPd43TW8uPrgNQGBdSN7KJlhO'
access_token = '960607027-xQIy6UihgeEwJf53IsAzodpWCXrCz2Dse431jWrs'
access_secret = 'SDngWBBCuyG2HlauGZD9FJ8IadsD2kZL6hX1jisliRc74'

 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True)

import csv
# Open/Create a file to append data
csvFile = open('result2.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

tweets = tweepy.Cursor(api.search, q="#ClimateChange-filter:retweets",
                          count=100,lang="en", since = "2017-12-31")
    
for tweet in tweets.items():
    #Write a row to the csv file: encode utf-8
    csvWriter.writerow([tweet.id_str, tweet.created_at, tweet.text.encode('utf-8'), 
                        tweet.favorite_count, tweet.retweet_count]) 
    print(tweet.created_at, tweet.text)
csvFile.close()




