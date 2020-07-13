from django.shortcuts import render
from appTwo.models import User
from appTwo import forms

# Create your views here.

def index(request):
    my_dict = {'insert_this': "This is inserted from the view.py file"}
    return render(request, 'home/homepage.html', context = my_dict)

def users(request):
    user_list = User.objects.order_by('-email')
    user_dict = {'user_rec': user_list}
    return render(request, 'appTwo/users.html', context = user_dict)




def signup_form(request):
    some_dict = forms.UserForm()

    if request.method == "POST":
        some_dict = forms.UserForm(request.POST)

        if some_dict.is_valid():
            print('VALIDATION SUCCSESS')
            f = some_dict.save()
            return index(request)

    return render(request, 'appTwo/signup.html', context = {'signup':some_dict})
