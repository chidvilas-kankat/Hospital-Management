from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import auth

# Create your views here.
class Authentication:

    @staticmethod
    def authenticate(request):
        return render(request, "login.html")

    @staticmethod
    def logIn(request):

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse("logged in")
        return HttpResponse("login failed")
