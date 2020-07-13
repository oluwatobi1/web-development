from django.urls import path
from helpapp import views

app_name = 'some'
urlpatterns = [
    path('', views.help, name = 'help')
]
