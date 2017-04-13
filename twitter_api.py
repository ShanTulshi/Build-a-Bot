import oauth2 as oauth
import json

#twitter_handle should NOT include the '@' symbol
def get_tweets(twitter_handle):
    CONSUMER_KEY = 'YurZ2aWgVEYVhE5c60XyWRGG0'
    CONSUMER_SECRET = 'TIaSl3xnVTNUzHrwz84lOycTYkwe9l1NocwkB4hGbd2ngMufn6'
    ACCESS_KEY = '564268368-tRdDLN3O9EKzlaY28NzHCgNsYJX59YRngv3qjjJh'
    ACCESS_SECRET = 'VUjRU2ftlmnUdqDtppMiV6LLqT83ZbKDDUjcpWtrT1PG4'

    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, access_token)

    endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=from%3A" + twitter_handle + "&result_type=all"
    response, data = client.request(endpoint)

    tweet_data = json.loads(data.decode('utf-8'))
    tweets = []
    for tweet in tweet_data['statuses']:
        tweets.append(tweet['text'] + ' \n')
    return tweets

#example
print(get_tweets("Cmdr_Hadfield"))
