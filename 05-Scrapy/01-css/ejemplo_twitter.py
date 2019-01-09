import twitter
api = twitter.Api(consumer_key='efICNJzBNU8dhExJWdtTCy7rn' ,
                  consumer_secret='GkwXVlHEnRN53tOhu8aHcnnWO5PnlGhZK8uwrSOwd8LVxMp7OA',
                  access_token_key='222932794-ZReC6KvWfxSnRiZL5uSwhESkTUtaOhWtC8kUnpiP',
                  access_token_secret='9gfpdnnQnCxK4OL83RKJZ24DkSRHm0GprzifwVCEHgxZp')

results = api.GetSearch(
    raw_query="q=amigo")

print(results)