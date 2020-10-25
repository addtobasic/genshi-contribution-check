import tweepy
import datetime,sys,time
from key import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tmp = 'https://twitter.com/genshi0916/status/'
while True:
  now = datetime.datetime.now()
  # print(str(now.hour)+":"+str(now.minute)+" "+str(now.second))
  if now.hour == 0 and now.minute == 15 and now.second == 0:
    for tweet in tweepy.Cursor(api.search, q='genshi0916 contribution 0 '+str(now.day)).items(1):
      id = tweet.id
      # user_name = tweet.user.screen_name
      # tmp = 'https://twitter.com/'+user_name+'/status/'

      try:
        print("contribution数:0ってどういうことですか?????????????進捗出してください\n" + tmp + str(id))
        api.update_status("contribution数:0ってどういうことですか?????????????進捗出してください\n" + tmp + str(id))
        print("----sleep中です----")
        time.sleep(86000) #だいたい1日待つ
      except:
        print('error')
