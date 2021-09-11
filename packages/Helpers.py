import tweepy
from textblob import TextBlob
import json


def Read_JSON_File(filepath):
    print("Reading file content from file " + filepath)
    file = open("./JSON/auth.json")
    data = json.load(file)
    return data


def Initialize_Twitter_API(api_key, api_key_secret, access_token, access_token_secret):
    print("Initializing the twitter bot")
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    tweeter = tweepy.API(auth)
    return tweeter


def Calculate_Sentiment(text):
    print("Calculating sentiments")
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity
    return sentiment_score


def Get_Filtered_Tweet(tweeter, word, number_of_tweets):
    my_id = int(tweeter.me().id_str)
    print("Searching tweet with word " + word)
    tweets = tweeter.search(word, count=number_of_tweets, lang="en")
    filtered_tweets = []
    for tweet in tweets:
        if tweet.in_reply_to_status_id is None and tweet.author.id != my_id:
            if Calculate_Sentiment(tweet.text) >= 0 and not tweet.retweeted:
                filtered_tweets.append(tweet)
    return filtered_tweets


def Retweet_Tweet(tweeter, tweet):
    print("Retweeting tweet with id: " + str(tweet.id))
    if not (tweeter.get_status(tweet.id)).retweeted:
        tweeter.retweet(tweet.id)
        print("Retweet done")
    else:
        print("Already retweeted")