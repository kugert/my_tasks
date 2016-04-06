import urllib2
import json

vk_url = 'https://api.vk.com/method/%s&%s%s'

methods = {
    "get_user": 'users.get?user_id=',
    "get_friend_lst": 'friends.get?user_id='
}

version = 'v=5.50'

fields = 'fields=books,site,status,interests,music,movies,tv,sex,games,about,quotes'


class VkApi:
    def __init__(self, user_id='20403803'):
        self.user_id = user_id

    def request_generator(self, method):
        url = vk_url % (method + self.user_id, fields, version)
        request = urllib2.urlopen(url)
        data = json.loads(request.read())
        return data

    def get_user_info(self):
        '''
        :return dict()
        '''
        user_info = self.request_generator(methods["get_user"])
        return user_info['response'][0]

    def get_friends_lst(self):
        '''
        :return list()
        '''
        friends_lst = self.request_generator(methods["get_friend_lst"])
        return friends_lst['response']
