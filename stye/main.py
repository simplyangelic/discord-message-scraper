import requests
import json

def retrieve_messages(channelid):
    headers = {
        'authorization': 'token here'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value, '\n')

retrieve_messages('channelid here')