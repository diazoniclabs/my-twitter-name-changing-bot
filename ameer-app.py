# Short code
import tweepy
consumer_key = ''
consumer_secret = ''
access_token = '-'
secret_access_token = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, secret_access_token)
api = tweepy.API(auth)
print('Everything is fine')

import time
while True:
  user = api.get_user('Ameen91741779')
  f = user.followers_count
  api.update_profile(name=f'AMEER {f} Followers')
  print(f'AMEER {f} Followers')
  time.sleep(60)
