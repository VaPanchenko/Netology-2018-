import requests
import time
import os
from pprint import pprint

TOKEN = '9259bb238213f4ed023776acd8edcb759124116f1910a39ff3bcbf948da236fa11340a3a848c3fc72c4e9'


def get_freinds_list():

    params = {
        'access_token': TOKEN,
        'v': '5.78',
    }

    r = requests.get('https://api.vk.com/method/friends.get', params).json()['response']
    return [item for item in r['items']]


def friends_get_mutual():

    friend_list = get_freinds_list()
    friends_mutual_list = []

    for friend in friend_list:

        params = {
            'access_token': TOKEN,
            'v': '5.78',
            'target_uid': friend,
        }

        r = requests.get('https://api.vk.com/method/friends.getMutual', params).json()['response']
        friends_mutual_list.append({'friend': friend, 'url_friend': f'https://vk.com/id{friend}', 'mutual_fiends': r})

        for f in r:
            friends_mutual_list.append({'mutual_friends_url': f'https://vk.com/id{f}'})

        time.sleep(0.1)

    return friends_mutual_list


pprint(friends_get_mutual())

output_file = os.path.join('result.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(str(friends_get_mutual()))

