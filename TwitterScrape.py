import tweepy

# Keys that are needed to access Twitter API via
consumer_key = "ADD CONSUMER KEY"
consumer_secret = "ADD CONSUMER SECRET"
access_token = "ADD ACCESS TOKEN"
access_token_secret = "ADD ACCESS TOKEN SECRET"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print_count = 0;
public_tweets = api.home_timeline(count = 100)
for tweet in public_tweets:
    print(tweet)
    print_count += 1

print (print_count)