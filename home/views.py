from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View 
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.db import IntegrityError
from django.views.generic import DetailView, ListView
from django.http import JsonResponse
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required


from .models import *
import json

class Auth(View):
    # Login get view
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("index"))

        next_ = request.GET.get("next", False)

        return render(request, "login.html", {
            "next": next_
        })
    
    # Login post view
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        next_ = request.POST.get("next", False)

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if next_:
                return redirect(next_)

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
        try:
            user = User.objects.create_user(username=username, first_name=fname, last_name=lname, password=password)
            if pfp is not None:
                user.profile_photo = pfp
            user.save()
        except IntegrityError as e:
            return render(request, "register.html", {
                "message": "User already exists, Please sign in"
            })
        login(request, user)

        request.session['just_created'] = True
        
        return redirect(reverse("author", kwargs={'username':username}))
        

class HomePageView(ListView):
    model = Blog
    template_name = "home.html"
    context_object_name = "articles"
   


class AuthorDetailView(View):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)

        message = request.session.get("message", False)
        just_created = request.session.get("just_created", False)

        if message:
            del request.session['message']
            
        if just_created:
            del request.session['just_created']
        

        return render(request, "author_detail.html", {
            "author":user,
            "just_created":just_created,
            "message": message
        })
    
    def post(self, request, username):
        data = request.POST

        user = request.user
        try:
            user.first_name = data['fname'].title()
            user.last_name = data['lname'].title() 
            user.profile_photo = data['pfp'] if data['pfp'] else DEFAULT_PFP
        except:
            pass
        user.about = data['about']

        user.save()
        request.session['message'] = "Profile details updated successfully"

        return redirect(reverse("author", kwargs={'username':user.username}))

class ArticleDetailView(DetailView):
    model = Blog
    context_object_name = "article"
    template_name = "article.html"

decorator = login_required(login_url=reverse_lazy("login"))
auth_required = method_decorator(decorator)
class ArticleCreateView(View):
    @auth_required
    def get(self, request):
        return render(request, "create_article.html")


def test(request, pk):
    print(request.path)
    return HttpResponse("Yes")

class API:
    """ Class that handles all the put requests """

    @staticmethod
    def edit_profile(request):
        pass
