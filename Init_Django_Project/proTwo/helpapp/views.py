from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def help(request):
    the_dict = {'something_here':"This sentence is injected into the page from the help app"}
    return render(request, 'helpapp/helppage.html', context = the_dict)
