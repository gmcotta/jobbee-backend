from django.shortcuts import get_object_or_404
from django.db.models import Avg, Min, Max, Count
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .serializers import SignUpSerializer, UserSerializer

# Create your views here.


@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data=data)
    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['email'],
                email=data['email'],
                password=make_password(data['password']),
            )
            return Response(
                {'message': 'User registered'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'error': 'User already exists.'},
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(user.errors)
