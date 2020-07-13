from django.urls import path
from . import views

urlpatterns = [
    path('forms/', views.forms_view, name = 'forms_view')
]
