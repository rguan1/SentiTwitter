from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from dateutil import parser
from flask_marshmallow import Marshmallow


# AlchemyServer.py hosts the code that interacts with our server which is either an sqlite server  (testing)
#  or mysql server (production). AlchemyServer also is also intended to maintain our api endpoint so that our clients can access our tweet data.
#  We are using flask, sqlAlchemy, and Marshmallow.

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

    def __repr__(self):
        return '<Tweet %r | %r | %r>' % (self.name, self.createdAt, self.fullText)


class TweetSchema(ma.ModelSchema):
    class Meta:
        model = Tweet



def add_tweet(name, twitterId, createdAt, fullText):
    datetimePythonFormat = parser.parse(createdAt)
    newTweet = Tweet(name=name, twitterId=twitterId, createdAt=datetimePythonFormat, fullText=fullText)
    db.session.add(newTweet)
    db.session.commit()
