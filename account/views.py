from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(["POST"])
def logout_user(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                request.user.auth_token.delete()
                return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)
            except Token.DoesNotExist:
                return Response({"Message": "Token does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"Message": "User is not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(["POST",])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Account has been created'
            data['username'] = account.username
            data['email'] = account.email
            
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            
            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh' : str(refresh),
                'access' : str(refresh.access_token)
            }
            
            
        else:
            data=serializer.errors
        return Response(data)