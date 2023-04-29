from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("robots.txt", views.robots_txt),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path("about/", views.about, name='about'),
    path("skills/", views.skills, name='skills'),
    path("contact/", views.contact, name='contact'),
    path("u/<str:username>/", views.profileView, name="profile"),
    path("blogs/", views.blogView, name="posts"),
    path("blogs/<slug:slug>/", views.blogFull, name="post_detailed"),
]