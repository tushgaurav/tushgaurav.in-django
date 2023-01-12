from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path("about/", views.about, name='about'),
    path("skills/", views.skills, name='skills'),
    path("contact/", views.contact, name='contact'),
    path("blogs/", views.postView, name="posts"),
    path("blogs/<slug:slug>/", views.postDetail, name="post_detailed"),

    path("<str:any>/", views.not_found, name='not-found')
]