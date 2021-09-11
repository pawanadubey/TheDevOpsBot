from packages.Helpers import *
import time

appConfig = Read_JSON_File("./JSON/auth.json")

tweeter = Initialize_Twitter_API(
    appConfig["api_key"],
    appConfig["api_key_secret"],
    appConfig["access_token"],
    appConfig["access_token_secret"],
)

while True:
    try:
        tweets = Get_Filtered_Tweet(tweeter, "devops", 20)
        for tweet in tweets:
            Retweet_Tweet(tweeter, tweet)
    except Exception as err:
        print("Error: " + str(err))
    time.sleep(10)