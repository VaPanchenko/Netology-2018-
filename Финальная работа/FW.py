import requests
import progressbar
import time
import json


Deleted_User = 18
Access_Denied = 15
Internal_server_error = 10
Permission_Denied = 7
Too_many_requests_per_second = 6


class DeletedUser(Exception):
    pass


class AccessDenied(Exception):
    pass


class UnknownError(Exception):
    pass


class PermissionDenied(Exception):
    pass


with open('user.json', 'r', encoding='utf8') as file:
    config = json.load(file)

user = config['user']
v = config['v']
TOKEN = config['TOKEN']
API_URL = 'https://api.vk.com/method/'


def do_api_call(api, params=None):

    params = params or {}
    params['access_token'] = TOKEN
    params['v'] = v

    while True:

        result = requests.get(API_URL + api, params=params).json()

        if 'error' in result:
            if result['error']['error_code'] == Deleted_User:
                print(result['error']['error_msg'], 'user/group - ',
                        result['error']['request_params'][2]['value'])
                raise DeletedUser()
            elif result['error']['error_code'] == Access_Denied:
                print(result['error']['error_msg'], 'user/group - ',
                        result['error']['request_params'][2]['value'])
                raise AccessDenied()
            elif result['error']['error_code'] == Internal_server_error:
                print(result['error']['error_msg'], 'user/group - ',
                        result['error']['request_params'][2]['value'])
                raise UnknownError()
            elif result['error']['error_code'] == Permission_Denied:
                print(result['error']['error_msg'], 'user/group - ',
                        result['error']['request_params'][2]['value'])
                raise PermissionDenied()
            elif result['error']['error_code'] == Too_many_requests_per_second:
                time.sleep(0.34)
                continue
            else:
                print(result)
                raise Exception
        else:
            break

    api_call_result = result['response']

    return api_call_result


def get_user_id():

    print('Получение User ID пользователя: {}'.format(user))

    try:
        r = do_api_call('users.get', params={'user_ids': user})
        result = r[0]['id']

    except (DeletedUser, UnknownError, PermissionDenied, AccessDenied):
        result = []

    return result


def get_friends(user_id):

    print('Получение списка друзей пользователя')

    try:
        r = do_api_call('friends.get', params={'user_id': user_id})
        result = r['items']

    except (DeletedUser, UnknownError, PermissionDenied, AccessDenied):
        result = []

    return result


def get_groups_target_user(user_id):

    print('Получение списка групп пользователя')
    try:
        r = do_api_call('groups.get', params={'user_id': user_id})
        result = r['items']
    except (DeletedUser, UnknownError, PermissionDenied, AccessDenied):
        result = []

    return result


def get_groups(friends):

    print('Формирование словаря групп друзей пользователя')
    groups = {}
    bar = progressbar.ProgressBar(max_value=len(friends))

    for i, friend in enumerate(friends):
        try:
            r = do_api_call('groups.get', params={'user_id': friend})
            groups.update({friend: r['items']})
            bar.update(i)
        except (DeletedUser, UnknownError, PermissionDenied, AccessDenied):
            continue

    return groups


def get_user_groups_info(difference_user_groups):

    groups_user_list_info = []
    info_list = []
    print('\nПолучение данных об уникальных группах пользователя')

    group_list = [difference_user_groups[i:i + 500] for i in range(0, len(difference_user_groups), 500)]

    for group in group_list:
        group = ', '.join([str(i) for i in group])

        try:
            group_info = do_api_call('groups.getById', params={'group_ids': group, 'fields': 'members_count'})

        except (DeletedUser, UnknownError, PermissionDenied, AccessDenied):
            continue

        groups_user_list_info.extend(group_info)

    for group in groups_user_list_info:

        info_list.append({'gid': group['id'], 'name': group['name'],
                            'members_count': group['members_count']})

    return info_list


def main():

    user_id = get_user_id()
    friends = get_friends(user_id)
    user_groups = set(get_groups_target_user(user_id))
    user_friends_group = get_groups(friends)
    union_friends_groups = set()

    for i in user_friends_group:
        union_friends_groups = union_friends_groups.union(set(user_friends_group.get(i)))

    difference_user_groups = list(user_groups.difference(union_friends_groups))

    result = get_user_groups_info(difference_user_groups)

    with open('groups.json', 'w', encoding='utf8') as file:
        json.dump(result, file,  ensure_ascii=False)


main()

