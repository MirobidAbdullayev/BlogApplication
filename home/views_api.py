from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 200
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'invalid username, user not found'
                raise Exception('invalid username not found')

        except Exception as e :
            print(e)
        return Response(response)