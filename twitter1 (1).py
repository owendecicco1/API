import keys
import tweepy
import json

#from tweetutilities import print_tweets

auth = tweepy.OAuthHandler(keys.api_key, keys.api_key_secret)

auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Success!")
except:
    print("Failed!")


keywords = "alexjones"
result_type = "popular"

tweets = api.search_tweets(keywords, lang = "en", result_type = result_type, count = 10)

query = "#collegefootball"

tweets = api.search_tweets(query, lang = "en", result_type = result_type, count = 10)
#print(tweets[0])
#outfile = open("output.json","w")
#json.dump(tweets,outfile,indent = 5)

#for tweet in tweets:
    #print(tweet.user.screen_name, ":", tweet.text, "\n\n")
    #input()

NewYork = 2459115

Dallas = 2388929

Waco = 2512937

World = 1

trends_available = api.get_place_trends(id = World)
print(trends_available)

outfile = open("trends.json","w")
json.dump(trends_available,outfile,indent = 5)

trends_list = trends_available[0]['trends']


trends_list = [t for t in trends_list if t['tweet_volume'] ]
#expression, iteration 
from operator import itemgetter 

trends_list.sort(key=itemgetter("tweet_volume"), reverse = True)

topics = {}

for t in trends_list:
    topics [t["name"]] = t["tweet_volume"]




from wordcloud import WordCloud

wc = WordCloud( width = 1600,
    height = 900,
    prefer_horizontal = 0.5,
    min_font_size = 10,
    colormap = "prism",
    background_color = "white",
)


wc = wc.fit_words (topics)

wc = wc.to_file("TrendingTopics.png")


