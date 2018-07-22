import requests
import progressbar
import time

user = 'tim_leary'
v = '5.78'
TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'


def get_user_id():

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_ids': user,
    }

    user_id = requests.get('https://api.vk.com/method/users.get', params=params).json()['response'][0]['id']

    return user_id


def get_friends(user_id):

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_id': user_id,
    }

    friends = requests.get('https://api.vk.com/method/friends.get', params=params).json()['response']['items']

    return friends


def get_groups_target_user(user_id):

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_id': user_id,
    }

    groups = requests.get('https://api.vk.com/method/groups.get', params=params).json()['response']['items']

    return groups


def get_groups(friends):

    groups = {}
    bar = progressbar.ProgressBar(max_value=len(friends))

    for i, friend in enumerate(friends, start=880):
        try:
            params = {
                'access_token': TOKEN,
                'v': v,
                'user_id': friend,
            }

            groups.update({friend: requests.get('https://api.vk.com/method/groups.get', params=params).json()['response']['items']})

            time.sleep(1)
            bar.update(i)

        except:
            continue

    return groups



user_id = get_user_id()
friends = get_friends(user_id)
print(get_groups_target_user(user_id))
groups = get_groups(friends)
print(groups)


