from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'post_list'),
    path('about/' , views.AboutView.as_view(), name = 'about')
]
