from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PalindromeGame, UserProfile

class PalindromeGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalindromeGame
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
