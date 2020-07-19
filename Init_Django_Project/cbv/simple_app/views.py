from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

# Create your views here.
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'simple_app/school_list.html'

class SchoolDetailView(DetailView):
    context_object_name = 'schools_detail'
    model = models.School

    template_name = 'simple_app/school_details.html'



class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['insert'] = 'I am being inserted!'
        return context
