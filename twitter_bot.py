import tweepy
import time 

auth=tweepy.OAuthHandler("?", "?")

auth.set_access_token('?','?')

api=tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user=api.me()

print(user) 
print(user.screen_name)

print('-------------------')
# for follower in tweepy.Cursor(api.followers).items():
#     # print(follower.name)
#     if follower.name=='Bollywoodbinge':
#         follower.follow()
    
print('-------------------')
    
    
search='Arvind Kejriwal'
tweets=400
for tweet in tweepy.Cursor(api.search,search).items(tweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)    
    except tweepy.TweepError as e:
        print(e.reason)
    
    except StopIteration:
        break
    
    
    
    
    
    
        

