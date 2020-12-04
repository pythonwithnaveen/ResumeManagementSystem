from django.contrib import admin
from django.urls import path
from process import views

urlpatterns = [
    path('',views.showIndex,name='main_page'),
    path('registration/',views.registration,name='registration'),
    path('user_registration/',views.registration,name='user_registration'),
]
