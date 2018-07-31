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

            time.sleep(0.34)
            bar.update(i)

        except (KeyError, ValueError):
            continue

    return groups




def get_user_groups_info(union_user_groups):

    groups_user_list_info = []
    print('\nПолучение данных об уникальных группах пользователя')

    group_list = [union_user_groups[i:i + 10] for i in range(0, len(union_user_groups), 10)]

    print(type(group_list))
    print(group_list[0])


    for i, group in enumerate(group_list):
        info_list = dict()

        params = {
            'access_token': TOKEN,
            'v': v,
            'group_ids': group,
            'fields': 'members_count'
        }


        group_info = requests.get('https://api.vk.com/method/groups.getById',
                                        params=params).json()['response'][0]


        print(type(group_info))
        print(group_info)

        groups_user_list_info.append(group_info)
        time.sleep(0.33)
        # print(groups_user_list_info)


    # bar = progressbar.ProgressBar(max_value=len(union_user_groups))

    # for i, group in enumerate(union_user_groups):
    #     try:
    #         info_list = dict()
    #
            # params = {
            #     'access_token': TOKEN,
            #     'v': v,
            #     'group_id': group,
            #     'fields': 'members_count'
            # }
    #         while True:
    #
                # group_info = requests.get('https://api.vk.com/method/groups.getById',
                #                       params=params).json()['response'][0]
    #             if group_info:
    #                 break
    #
    #         info_list['gid'] = group_info['id']
    #         info_list['name'] = group_info['name']
    #         info_list['members_count'] = group_info['members_count']
    #
    #         groups_user_list_info.append(info_list)
    #
    #         bar.update(i)
    #
    #     except (KeyError, ValueError):
    #         continue

    return groups_user_list_info


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


# main()

user_id = get_user_id()

group = get_groups_target_user(user_id)


print('___________________________')
print(get_user_groups_info(group))


