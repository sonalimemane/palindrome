from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import PalindromeGame, UserProfile
from .serializers import PalindromeGameSerializer, UserSerializer, UserProfileSerializer

class PalindromeGameCreate(generics.CreateAPIView):
    queryset = PalindromeGame.objects.all()
    serializer_class = PalindromeGameSerializer
    permission_classes = [permissions.IsAuthenticated]

class PalindromeGameCheck(generics.RetrieveUpdateAPIView):
    queryset = PalindromeGame.objects.all()
    serializer_class = PalindromeGameSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserProfileUpdate(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
