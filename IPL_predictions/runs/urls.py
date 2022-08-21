from django.contrib import admin
from django.urls import path,include
from runs import views
urlpatterns = [
    path('',views.tosdic,name='winner'),
    path('tosdic',views.tosdic,name='winner'),
    path('tosswiner',views.toswinner,name='winner'),
    path('winner',views.winner,name='winnert'),
    # path('winner',views.winner,name='winnert'),
    path('run',views.runs,name='home'),
    path('result',views.runs,name='result')
]