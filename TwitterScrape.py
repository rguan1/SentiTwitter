import tweepy
from tweepy import RateLimitError
import json

#Note, this should be removed from your program! This is just a way of hiding our key while still using github
#publically. Likewise TwitterPwdGrabber.(whatever key/token) should be replaced by your own key and tokens.
import TwitterPwdGrabber

# Keys that are needed to access Twitter API via
# consumer_key = "ADD CONSUMER KEY"
# consumer_secret = "ADD CONSUMER SECRET"
# access_token = "ADD ACCESS TOKEN"
# access_token_secret = "ADD ACCESS TOKEN SECRET"


consumer_key = TwitterPwdGrabber.consumer_key
consumer_secret = TwitterPwdGrabber.consumer_secret
access_token = TwitterPwdGrabber.access_token
access_token_secret = TwitterPwdGrabber.access_token_secret


def simple_home_timeline_scrape():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    print_count = 0;
    public_tweets = api.home_timeline(since_id = 1020315883451965440, count = 100)
    for tweet in public_tweets:
        print(tweet)
        print_count += 1

    print(print_count)

#Don't forget to fix this dumbass program!
def parsed_json_home_timeline_scrape():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    try:
        public_tweets = api.home_timeline(since_id=1020315883451965440, count=100, tweet_mode='extended')
        for tweet in public_tweets:
            jsonDict = tweet._json
            # print(jsonDict["created_at"] + " " + jsonDict["full_text"])
            print(tweet)

    except RateLimitError:
        print("You've exceeded the rate that we are allowed to pull from")


def main():
    parsed_json_home_timeline_scrape()

if __name__ == '__main__':
    main()