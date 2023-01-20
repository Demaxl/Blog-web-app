from django.shortcuts import render, HttpResponse, redirect
from django.views import View 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Blog

class Auth(View):
    # Login get view
    def get(self, request):
        return render(request, "login.html")
    
    # Login post view
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid email and/or password"
            })


    @staticmethod
    def logout_view(request):
        logout(request)

        return redirect(reverse("index"))

class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")
    
    def post(self, request):
        data = request.POST

        username = request.POST['username']
        fname = data['fname'].title()
        lname = data['lname'].title()
        pfp = data['pfp'] if data['pfp'] else None
        password = data['password']

         # Attempt to create new user
        # try:
        user = User.objects.create_user(username=username, first_name=fname, last_name=lname, password=password)
        if pfp is not None:
            print(pfp)
            user.profile_photo = pfp
        user.save()
        # except IntegrityError as e:
        #     return render(request, "register.html", {
        #         "message": "User already exists, Please sign in"
        #     })
        login(request, user)
        
        return redirect(reverse("index"))
        

class HomePageView(View):
    def get(self, request):
        return render(request, "home.html")


