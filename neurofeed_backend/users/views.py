from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import CustomUser
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        full_name = request.data.get('full_name', '')

        if not username or not email or not password:
            return Response(
                {'error': 'username, email and password are required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if CustomUser.objects.filter(email=email).exists():
            return Response(
                {'error': 'Email already registered'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = CustomUser.objects.create(
            username=username,
            email=email,
            password=hash_password(password),
            full_name=full_name
        )

        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'message': 'Account created successfully'
        }, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = CustomUser.objects.get(
                email=email,
                password=hash_password(password)
            )
            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'message': 'Login successful'
            })
        except CustomUser.DoesNotExist:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )