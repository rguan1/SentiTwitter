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

    # returns a value between -1 and 1. -1 is very negative and 1 is very positive
    def sentiAnalysis(self, tweetText):
        textB = TextBlob(tweetText)
        return textB.sentiment.polarity

    def parsed_json_home_timeline_scrape(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)
        try:
            public_tweets = None
            if AlchemyServer.is_database_empty():
                public_tweets = api.home_timeline(tweet_mode='extended', count=200)
            else:
                db_since_id = AlchemyServer.get_largest_id_tweet()
                public_tweets = api.home_timeline(since_id=db_since_id, tweet_mode='extended')

            for tweet in public_tweets:
                jsonDict = tweet._json
                fakeSentimentRating = self.sentiAnalysis(jsonDict['full_text'])

                # This adds the tweet to database!!
                AlchemyServer.add_tweet(
                    name=jsonDict['user']['name'],
                    twitterId=jsonDict['id'],
                    createdAt=jsonDict['created_at'],
                    fullText=jsonDict['full_text'],
                    sentimentRating=fakeSentimentRating)

                print(jsonDict['user']['name'] + " " + jsonDict["created_at"] + " " + jsonDict['full_text'])

        except RateLimitError:
            print("You've exceeded the rate that we are allowed to pull from")
