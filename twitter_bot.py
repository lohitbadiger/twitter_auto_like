import tweepy
import time 

auth=tweepy.OAuthHandler("oJi7djtEZBPrml73GnyinxJcA", "FXxSfCGy5kGgLlWLUp9Y4lJ6003fOrbxlBHm0V9CsbBnHjq41P")

auth.set_access_token('771714774031675393-zA7wvv0VcB3Pxg0ZwYFELjdMTJOVHxO','JCMZBFMLG9nfFmXgc06s0v3IamUJc2vGtIm95uIlBxCDz')

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
    
    
    
    
    
    
        

