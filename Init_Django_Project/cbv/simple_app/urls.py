from django.urls import path
from simple_app import views

app_name = 'simple_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name = 'list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name = 'detail'),
    path('updateschool/<int:pk>', views.SchoolUpdateView.as_view(), name = 'updateschool'),
    path('createschool/', views.SchoolCreateView.as_view(), name = 'createschool'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name = "delete"),

    path('student_list', views.StudentListView.as_view(), name = 'student_list'),
    path('createstudent/', views.StudentCreateView.as_view(), name = 'createstudent'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name = 'student_detail'),

    path('updatestudent/<int:pk>', views.StudentUpdateView.as_view(), name = 'updatestudent'),
    path('deletestudent/<int:pk>', views.StudentDeleteView.as_view(), name = 'deletestudent')

]
