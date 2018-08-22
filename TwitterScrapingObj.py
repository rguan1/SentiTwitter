import tweepy
from tweepy import RateLimitError
from textblob import TextBlob
import AlchemyServer

#Note, this should be removed from your program! This is just a way of hiding our key while still using github
#publically
import TwitterPwdGrabber

# Keys that are needed to access Twitter API via
# consumer_key = "ADD CONSUMER KEY"
# consumer_secret = "ADD CONSUMER SECRET"
# access_token = "ADD ACCESS TOKEN"
# access_token_secret = "ADD ACCESS TOKEN SECRET


consumer_key = TwitterPwdGrabber.consumer_key
consumer_secret = TwitterPwdGrabber.consumer_secret
access_token = TwitterPwdGrabber.access_token
access_token_secret = TwitterPwdGrabber.access_token_secret


class TwitterScraper:
    def __init__(self):
        self.max_id = None

    def sentiAnalysis(self): #returns a value between -1 and 1. -1 is very negative and 1 is very positive
        textb=TextBlob(self)
        return textb.sentiment.polarity

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

                    #Sentiment constant. Should be replaced by an actual calculator
                    fakeSentimentRating = sentiAnalysis(json.dumps(jsonDict["full_text"]))

                    #This adds the tweet to database!!
                    AlchemyServer.add_tweet(
                        name=jsonDict['user']['name'],
                        twitterId=jsonDict['id'],
                        createdAt=jsonDict['created_at'],
                        fullText=jsonDict['full_text'],
                        sentimentRating=fakeSentimentRating)

                    print(jsonDict['user']['name'] + " " + jsonDict["created_at"] + " " + jsonDict['full_text'])
        except RateLimitError:
            print("You've exceeded the rate that we are allowed to pull from")
