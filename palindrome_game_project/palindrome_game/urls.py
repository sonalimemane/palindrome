from django.urls import path
from .views import PalindromeGameCreate, PalindromeGameCheck, UserCreate, UserDelete, UserProfileUpdate

urlpatterns = [
    path('games/', PalindromeGameCreate.as_view(), name='game-create'),
    path('games/<int:pk>/', PalindromeGameCheck.as_view(), name='game-check'),
    path('register/', UserCreate.as_view(), name='user-create'),
    path('users/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
    path('profile/<int:pk>/update/', UserProfileUpdate.as_view(), name='user-profile-update'),
]
