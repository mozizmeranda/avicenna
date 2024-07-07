from rest_framework import viewsets, generics
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import *
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime


class UserViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        number = request.data['number']
        user = User.objects.filter(number=number).first()

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret')
        # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZXhwIjoxNzIwMTk2MDEzLCJpYXQiOjE3MjAxOTI0MTN9.E3vfHYPzcRrRxos7vyk6ZlTl7qZWsdlmh5SJgVP7rYk
        response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "token": token
        }
        return response
        # return Response(serializer.data)


class LoginView(viewsets.ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        data = self.request.data
        return data

    def post(self, request):
        number = request.data['number']
        password = request.data['password']

        user = User.objects.filter(number=number).first()
        if user is None:
            raise AuthenticationFailed("User is not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret')
        # eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiZXhwIjoxNzIwMTk2MDEzLCJpYXQiOjE3MjAxOTI0MTN9.E3vfHYPzcRrRxos7vyk6ZlTl7qZWsdlmh5SJgVP7rYk
        response = Response()
        # response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "token": token
        }
        return response


class UserView(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        token = self.request.headers.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, 'secret', options={"verify_signature": False})
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token is not valid")

        user = User.objects.filter(id=payload['id'])

        return user
