from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("skills/", views.skills, name='skills'),

    path("<str:any>/", views.not_found, name='not-found')
]