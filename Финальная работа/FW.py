import requests
import progressbar
import time
import json


with open('user.json', 'r', encoding='utf8') as file:
    data = json.load(file)

user = data['user']
v = data['v']
TOKEN = data['TOKEN']


def get_user_id():

    print('Получение User ID пользователя: {}'.format(user))

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_ids': user,
    }

    while True:
        user_id = requests.get('https://api.vk.com/method/users.get',
                               params=params).json()['response'][0]['id']
        if user_id:
            break

    return user_id


def get_friends(user_id):

    print('Получение списка друзей пользователя')

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_id': user_id,
    }

    while True:
        friends = requests.get('https://api.vk.com/method/friends.get',
                               params=params).json()['response']['items']
        if friends:
            break

    return friends


def get_groups_target_user(user_id):

    print('Получение списка групп пользователя')

    params = {
        'access_token': TOKEN,
        'v': v,
        'user_id': user_id,
    }

    while True:
        groups = requests.get('https://api.vk.com/method/groups.get',
                          params=params).json()['response']['items']
        if groups:
            break

    return groups


def get_groups(friends):

    print('Формирование словаря групп друзей пользователя')
    groups = {}
    bar = progressbar.ProgressBar(max_value=len(friends))
    d = dict()

    for i, friend in enumerate(friends):
        try:
            params = {
                'access_token': TOKEN,
                'v': v,
                'user_id': friend,
            }
            while True:

                groups.update({friend: requests.get('https://api.vk.com/method/groups.get',
                                                 params=params).json()['response']['items']})
                if groups:
                    break
                print(type(groups.get(88220)))


            bar.update(i)
            time.sleep(0.33)

        except Exception as e:
            if e == (KeyError or ValueError):
                continue
            else:
                print(friend)
                print(Exception)
                continue


    return groups


def get_user_groups_info(union_user_groups):

    groups_user_list_info = []
    info_list = []
    print('\nПолучение данных об уникальных группах пользователя')

    group_list = [union_user_groups[i:i + 500] for i in range(0, len(union_user_groups), 500)]
    bar = progressbar.ProgressBar(max_value=len(group_list))

    for group in group_list:
        group = [(', '.join([str(i) for i in group]))]

        params = {
            'access_token': TOKEN,
            'v': v,
            'group_ids': group,
            'fields': 'members_count'
        }

        while True:
            group_info = requests.get('https://api.vk.com/method/groups.getById',
                         params=params).json()['response']
            if group_info:
                break

        groups_user_list_info.append(group_info)

        bar.update(group)
        time.sleep(0.34)

    for i in range(len(union_user_groups)):

        info_list.append({'gid': groups_user_list_info[0][i]['id'], 'name': groups_user_list_info[0][i]['name'],
                     'members_count': groups_user_list_info[0][i]['members_count']})

    return info_list


def main():

    user_id = get_user_id()
    friends = get_friends(user_id)
    user_groups = set(get_groups_target_user(user_id))
    user_friends_group = get_groups(friends)
    union_friends_groups = set()

    for i in user_friends_group:
        union_friends_groups = union_friends_groups.union(set(user_friends_group.get(i)))

    union_user_groups = list(user_groups.difference(union_friends_groups))

    result = get_user_groups_info(union_user_groups)

    with open('groups.json', 'w', encoding='utf8') as file:
        json.dump(result, file,  ensure_ascii=False)


main()

