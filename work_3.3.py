class User():

    def __init__(self, us_id):
        self.us_id = us_id

    def __str__(self):
        return f'https://vk.com/id{self.us_id}'

user = User(35341148)
print(user)