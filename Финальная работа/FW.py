import requests
import progressbar
import time
import json

user = 'tim_leary'
v = '5.78'
TOKEN = '7b23e40ad10e08d3b7a8ec0956f2c57910c455e886b480b7d9fb59859870658c4a0b8fdc4dd494db19099'


def get_user_id():

    print('Получение User ID пользователя: {}'.format(user))

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_ids': user,
    }
    user_id = requests.get('https://api.vk.com/method/users.get',
                           params=params).json()['response'][0]['id']

    return user_id


def get_friends(user_id):

    print('Получение списка друзей пользователя')

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_id': user_id,
    }
    friends = requests.get('https://api.vk.com/method/friends.get',
                           params=params).json()['response']['items']

    return friends


def get_groups_target_user(user_id):

    print('Получение списка групп пользователя')

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_id': user_id,
    }
    groups = requests.get('https://api.vk.com/method/groups.get',
                          params=params).json()['response']['items']

    return groups


def get_groups(friends):

    print('Формирование словаря групп друзей пользователя')
    groups = {}
    bar = progressbar.ProgressBar(max_value=len(friends))

    for i, friend in enumerate(friends):
        try:
            params = {
                'access_token': TOKEN,
                'v': v,
                'user_id': friend,
            }

            groups.update({friend: requests.get('https://api.vk.com/method/groups.get',
                                                params=params).json()['response']['items']})

            time.sleep(0.34)
            bar.update(i)
        except:
            continue

    return groups


def get_user_groups_info(union_user_groups):

    groups_user_list_info = []

    print('\nПолучение данных об уникальных группах пользователя')
    bar = progressbar.ProgressBar(max_value=len(union_user_groups))

    for i, group in enumerate(union_user_groups):
        try:
            info_list = dict()

            params = {
                'access_token': TOKEN,
                'v': v,
                'group_id': group,
                'fields': 'members_count'
            }

            group_info = requests.get('https://api.vk.com/method/groups.getById',
                                      params=params).json()['response'][0]

            info_list['gid'] = group_info['id']
            info_list['name'] = group_info['name']
            info_list['members_count'] = group_info['members_count']

            groups_user_list_info.append(info_list)

            # time.sleep(0.34)
            bar.update(i)

        except:
            continue

    return groups_user_list_info


def main():

    user_id = get_user_id()
    friends = get_friends(user_id)
    user_groups = set(get_groups_target_user(user_id))
    user_friends_group = get_groups(friends)
    super_group = set()

    for i in user_friends_group:
        super_group = super_group.union(set(user_friends_group.get(i)))

    union_user_groups = list(user_groups.difference(super_group))

    result = get_user_groups_info(union_user_groups)
    print(result)

    with open('groups.json', 'w', encoding='utf8') as file:
        json.dump(result, file,  ensure_ascii=False)


main()
