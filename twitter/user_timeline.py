import json
import time
from requests_oauthlib import OAuth1Session

from settings import (
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

user_timelines = []
status_sum = 0

oauth = OAuth1Session(
    CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

resource_url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

screen_name = 'sksk_sskn'
count = 200
max_id = 2000000000000000000

params = {'screen_name': screen_name, 'count': count, 'max_id': max_id}

while True:
    r = oauth.get(resource_url, params=params)

    user_timeline = json.loads(r.text)
    status_num = len(user_timeline)

    if not status_num:
        break
    print('get {} statuses'.format(status_num))

    user_timelines += user_timeline
    status_sum += status_num

    max_id = user_timeline[-1]['id'] - 1
    params['max_id'] = max_id

    time.sleep(1)

print('\nget {} statuses in total'.format(status_sum))

with open('user_timeline.json', 'w', encoding='utf-8') as f:
    json.dump(user_timelines, f, separators=(',', ':'))
