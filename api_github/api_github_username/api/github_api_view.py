import requests
from rest_framework.views import APIView
from rest_framework.response import Response

class ApiGithub(APIView):

    def get(self, request, username):


        url = f'https://api.github.com/users/{username}'
        r = requests.get(url)
        
        return Response(r.json())