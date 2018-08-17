from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dateutil import parser
from flask_marshmallow import Marshmallow


# AlchemyServer.py hosts the code that interacts with our server which is either an sqlite server  (testing)
#  or mysql server (production). AlchemyServer also is also intended to maintain our api endpoint so that our
# clients can access our tweet data. We are using flask, sqlAlchemy, and Marshmallow.

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    twitterId = db.Column(db.Integer, unique=True, nullable=False)
    createdAt = db.Column(db.DateTime)
    fullText = db.Column(db.Text)
    sentimentRating = db.Column(db.Float)

    def __repr__(self):
        return '<Tweet %r | %r | %r | %r>' % (self.name, self.createdAt, self.fullText, self.sentimentRating)


class TweetSchema(ma.ModelSchema):
    class Meta:
        model = Tweet

#Declaring schemas which are required by marshamllow
tweet_schema = TweetSchema()
tweets_schema = TweetSchema(many=True)


@app.route("/api/tweets", methods=["GET"])
def get_tweets():
    # all_tweets = Tweet.query.all()
    # return tweet_schema.jsonify(all_tweets)

    # alternative way according to flask-marshmallow docs
    all_tweets = Tweet.query.all()
    result = tweets_schema.dump(all_tweets)
    return jsonify(result.data)





def add_tweet(name, twitterId, createdAt, fullText, sentimentRating):
    datetimePythonFormat = parser.parse(createdAt)
    newTweet = Tweet(name=name,
                     twitterId=twitterId,
                     createdAt=datetimePythonFormat,
                     fullText=fullText,
                     sentimentRating=sentimentRating)
    db.session.add(newTweet)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True, port=8000)