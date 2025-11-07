from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = Response()
        response.data = serializer.data
        return response
    
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        user = get_object_or_404(User, email=email)
        password = request.data.get('password', None)
        is_check = user.check_password(password)
        if not is_check:
            raise AuthenticationFailed('Authentication failed')
        
        refesh = RefreshToken.for_user(user)
        access = refesh.access_token
        return Response({
            'refresh': str(refesh),
            'access': str(access),
        })