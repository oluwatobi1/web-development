from django.urls import path
from appTwo import views

app_name = 'appTwo'

urlpatterns = [
    path('', views.users, name = 'users')

]
