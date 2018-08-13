import tweepy
from tweepy import RateLimitError
import json

# Keys that are needed to access Twitter API via
# consumer_key = "ADD CONSUMER KEY"
# consumer_secret = "ADD CONSUMER SECRET"
# access_token = "ADD ACCESS TOKEN"
# access_token_secret = "ADD ACCESS TOKEN SECRET"


consumer_key = "2IrLEJjQjmLdXmScdOIxCcE9G"
consumer_secret = "Xn1xGV2nLc1JfJAatnkc89ktClLY5HR0d5JgX2U4Z9Xq8U6icy"
access_token = "1008908720657584128-COXHZz1ijC1SVTuYrAmEcjgS9eSzQR"
access_token_secret = "f8KWKG1h18w0C3YhHMNWDjOyjxuZChBJ16SNGHBczatOQ"


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
            print(jsonDict["created_at"] + " " + jsonDict["full_text"])

    except RateLimitError:
        print("You've exceeded the rate that we are allowed to pull from")


def main():
    parsed_json_home_timeline_scrape()

if __name__ == '__main__':
    main()