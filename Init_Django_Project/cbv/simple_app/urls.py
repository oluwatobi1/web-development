from django.urls import path
from simple_app import views

app_name = 'simple_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name = 'list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name = 'detail')

]
