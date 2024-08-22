from django.shortcuts import render
from django.views import View


class ProfileView(View):
    def get(self, request):
        return render(request, 'profile.html')


class SignIn(View):
    def get(self, request):
        return render(request, 'sign-in.html')


class SignUp(View):
    def get(self, request):
        return render(request, 'sign-up.html')