from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from . import models

# Create your views here.
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'simple_app/school_list.html'


class StudentListView(ListView):
    context_object_name = 'student_list'
    model = models.Student
    template_name = 'simple_app/student_list'

class SchoolDetailView(DetailView):
    context_object_name = 'schools_detail'
    model = models.School
    template_name = 'simple_app/school_details.html'

class StudentDetailView(DetailView):
    context_object_name = 'students_detail'
    model = models.Student
    template_name = 'simple_app/student_details.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name', 'owner', 'location')
    template_name = 'simple_app/school_form.html'

class StudentCreateView(CreateView):
    model = models.Student
    fields = '__all__'

# Updating views
class SchoolUpdateView(UpdateView):
    fields = ('name', 'owner')
    model = models.School

class StudentUpdateView(UpdateView):
    fields = ('student_name', 'school', 'grade_level')
    model = models.Student



class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insert'] = 'I am being inserted!'
        return context
