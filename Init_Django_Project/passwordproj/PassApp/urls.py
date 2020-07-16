from django.urls import path
from PassApp import views

app_name = 'passapp'

urlpatterns = [
    path('', views.register, name = 'register'),
    path('login/', views.userlogin, name = 'userlogin')
]
