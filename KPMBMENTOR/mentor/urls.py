from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path('newmentor', views.newmentor, name="newmentor"),
path("searchpage", views.searchpage, name="searchpage")

]