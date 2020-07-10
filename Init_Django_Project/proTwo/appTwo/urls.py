from django import path
from appTwo import views


urlpatterns = [
    path('', views.index, name = 'index')
]
