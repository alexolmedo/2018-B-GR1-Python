import tweepy
import jsonpickle
import pandas as pd

CONSUMER_KEY = 'efICNJzBNU8dhExJWdtTCy7rn'
CONSUMER_SECRET = 'GkwXVlHEnRN53tOhu8aHcnnWO5PnlGhZK8uwrSOwd8LVxMp7OA'
ACCESS_TOKEN = '222932794-ZReC6KvWfxSnRiZL5uSwhESkTUtaOhWtC8kUnpiP'
ACCESS_SECRET = '9gfpdnnQnCxK4OL83RKJZ24DkSRHm0GprzifwVCEHgxZp'


def obtener_api_twitter():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def harvest_tweets(filepath, api, query, max_tweets=100, lang='es'):
    tweetCount = 0
    with open(filepath, 'w') as f:
        for tweet in tweepy.Cursor(api.search,q=query,lang=lang).items(max_tweets):
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1
        print("Se descargaron {0} tweets".format(tweetCount))


def tweets_to_df(path):
    tweets = list(open('nvidia.json', 'rt'))

    text = []
    date = []
    screen_name = []

    for t in tweets:
        t = jsonpickle.decode(t)

        text.append(t['text'])
        date = t['created_at']

        screen_name.append(t['user']['screen_name'])

    d = {'text': text,
         'date': date,
         'screen_name': screen_name
         }

    return pd.DataFrame(data=d)





api = obtener_api_twitter()
query = '#nvidia'
harvest_tweets('nvidia.json', api, query)
tweets_df = tweets_to_df('nvidia.json')
tweets_df.to_csv("nvidia.csv", sep='\t', encoding='utf-8')