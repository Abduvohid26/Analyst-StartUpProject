from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('sign-in/', views.SignIn.as_view(), name = 'sign-in'),
    path('sign-up/', views.SignUp.as_view(), name = 'sign-up')
]