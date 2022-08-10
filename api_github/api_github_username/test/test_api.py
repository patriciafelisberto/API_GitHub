from django.test import TestCase
from django.test import Client

class User:
    def __init__(self):
        self.login = 'patriciafelisberto'
        self.id = 106412544
        self.avatar_url = 'https://avatars.githubusercontent.com/u/106412544?v=4'
        self.html_url = 'https://github.com/patriciafelisberto'

class TestApiGithubMethods(TestCase):

    def test_username_parameters(self):
        user = User()
        client = Client()
        response = client.get('/api/github/patriciafelisberto')
        paramenters = ['login', 'id', 'avatar_url', 'html_url']
        for param in paramenters:
            self.assertEqual(user.__dict__[param], response.data[param])
