from django.shortcuts import render, HttpResponse

from django.views import View 


class HomePageView(View):
    def get(self, request):
        return HttpResponse("<h1>AB Blog</h1>")
