from django.contrib.auth.models import User
from django.http import Http404
from api.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Account(APIView):
    def get_object(self,request):
        return User.objects.get(username=request.user.username)

    def get(self, request, format=None):
        user = self.get_object(request)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, format='json'):
        user = self.get_object(request)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#http -a username:password PUT localhost:3000/accounts/profile/ username=admin last_name=kumar
        

class NewUser(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

