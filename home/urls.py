from django.urls import path 
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("login/", views.Auth.as_view(), name="login"),
    path("logout/", views.Auth.logout_view, name="logout"),
    path("signup/", views.RegisterView.as_view(), name="register"),
    path("author/<slug:username>", views.AuthorDetailView.as_view(), name="author"),
    path("article/<int:pk>", views.ArticleDetailView.as_view(), name="article"),
    path("write/", views.ArticleCreateView.as_view(), name="create")

]
