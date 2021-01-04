from django.urls import path
from . import views

urlpatterns = [
    path('', views.allposts, name='allposts'),
]
