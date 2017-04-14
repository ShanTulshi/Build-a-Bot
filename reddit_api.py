import json
import requests

def get_comments(reddit_username):
    SECRET = 'Zn7Q6uj2KfarooUuK_jEoMEv0kg'
    headers = {"Authorization": "bearer 3rhJj1Zx1Hwu0p9djavecclBVpc", "User-Agent": "Build-A-Bot Markov Workshop by hannparkk"}
    endpoint = "https://oauth.reddit.com/user/" + reddit_username + "/comments/.json"
    response = requests.get(endpoint, headers=headers)
    r = json.loads(response.text)
    return r

print(get_comments('Avesplosion'))