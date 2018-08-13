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


class TwitterScraper:
    #since_id, max_id, count, page

    def __init__(self):
        self.max_id = None

    def parsed_json_home_timeline_scrape(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        try:
            public_tweets = None
            if (self.max_id is None):
                public_tweets = api.home_timeline(tweet_mode='extended')
            else:
                public_tweets = api.home_timeline(max_id=self.max_id, tweet_mode='extended')

            for tweet in public_tweets:
                jsonDict = tweet._json


                if self.max_id is None or self.max_id > jsonDict['id']:
                    self.max_id = jsonDict['id'] - 1
                    # print(jsonDict["id"] + " " + jsonDict["created_at"] + " " + jsonDict["full_text"])
                    print(jsonDict["created_at"] + " " + jsonDict['full_text'])
        except RateLimitError:
            print("You've exceeded the rate that we are allowed to pull from")
