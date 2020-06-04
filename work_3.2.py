import requests

token = "7a8283bac0bc1a6b42a9742d1a0fc7e6c2d398b5a15fa20a7698cb00a1fa1fd43070256335a2caffbe5ca"
url = 'https://api.vk.com/method/friends.get'

class User():

    def __init__(self, us_id):
        self.us_id = us_id
        self.params = {'v': 5.107,
                  'access_token': token,
                  'user_id': us_id}

    def __str__(self):
        return f'user id {self.us_id}'

    def all_list_friends(self):

        res = requests.get(url, params=self.params)
        list_friends = res.json()['response']['items']
        return set(list_friends)

    def __and__(self, other_user):

        mutual_list_friends = self.all_list_friends() & other_user.all_list_friends()
        return f'Список общих друзей {self} и {other_user}: {mutual_list_friends}'

us1 = User(35341148)
us2 = User(136221123)

eqal_friends = us1 & us2
print(eqal_friends)



