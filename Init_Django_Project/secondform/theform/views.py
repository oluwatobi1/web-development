from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request, 'home/homepage.html')

def forms_view(request):
    inst = forms.Form()
    sec = forms.StudentForm()
    if request.method == "POST":
        inst= forms.Form(request.POST)
        sec = forms.StudentForm(request.POST)

        if inst.is_valid() and sec.is_valid():
            print("Submitted successfully")
            f = inst.save()
            s = sec.save()
            return home(request)
    return render(request, 'form/form.html', context = {'form_html':inst, 'secf':sec})
