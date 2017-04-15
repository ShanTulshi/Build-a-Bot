import json
import requests

#TO GET AUTH TOKEN:
#curl -X POST -d 'grant_type=password&username=hannparkk&password=hp11241456' --user 'qhFPYj5Gy7LLgg:Zn7Q6uj2KfarooUuK_jEoMEv0kg' https://www.reddit.com/api/v1/access_token

def get_comments(reddit_username):
    SECRET = 'Zn7Q6uj2KfarooUuK_jEoMEv0kg'
    headers = {"Authorization": "bearer MKiE5F9xEthyS51_9Q30Dv2acC4", "User-Agent": "Build-A-Bot Markov Workshop by hannparkk"}
    endpoint = "https://oauth.reddit.com/user/" + reddit_username + "/comments/.json"
    response = requests.get(endpoint, headers=headers)
    r = json.loads(response.text)
    array = r[u'data'][u'children']
    comments = []
    for entry in array:
        comments.append(entry[u'data'][u'body'])
    return comments

#example
# print(get_comments('hannparkk'))
