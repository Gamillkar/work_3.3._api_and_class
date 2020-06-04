import requests

token = "7a8283bac0bc1a6b42a9742d1a0fc7e6c2d398b5a15fa20a7698cb00a1fa1fd43070256335a2caffbe5ca"

url = 'https://api.vk.com/method/friends.get'
list_users_id = []
list_final = []
class Users():
    """Описание пользователя с помощью класса и реализация метода поиска общих друзей"""
    def __init__(self, user_id):
        self.user_id = user_id
        list_users_id.append(user_id)

    def account_equal_quantity_friends(self):

        self.quantity_users_id = []

        for user in list_users_id:
            params = {'v': 5.107,
                      'access_token': token,
                      'user_id': user}
            res = requests.get(url, params=params)
            list_friends = res.json()['response']['items']
            self.quantity_users_id += list_friends

            for equal_id in self.quantity_users_id:
                if self.quantity_users_id.count(equal_id) == 2 and equal_id not in list_final:
                    list_final.append(equal_id)
        print(f'Количество общих друзей {len(list_final)}')



us1 = Users(35341148)
us2 = Users(136221123)
us1.account_equal_quantity_friends()




