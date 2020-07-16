from django.shortcuts import render
from PassApp.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'passapp\index.html')

def register(request):
    registered = False

    if request.method == "POST":
        userform = UserForm(data = request.POST)

        profileform = UserProfileForm(data = request.POST)

        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
# profile and profile_pics Variable name was swapped..
# to be corrected later

            profile_pics = profileform.save(commit = False)
            profile_pics.user = user

            if 'profile' in request.FILES:
                profile_pics.profile = request.FILES['profile']

            profile_pics.save()

            registered = True
            return HttpResponse("Registration Successful")
        else:
            print(user.errors, profile_pics.errors)
    else:
        userform = UserForm()
        profileform = UserProfileForm()

    return render(request, 'passapp/register.html', context = {'registered': registered,
                                                                'form_user':userform,
                                                                'form_profile':profileform})



def userlogin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password=password)
        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('special'))

            else:
                HttpResponse('USER NOT ACTIVE')
        else:
            print('Wrong login combo')
            return HttpResponse('INVALID LOGIN DETAILS')
    else:
        return render(request, 'passapp/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('WELCOME TO THIS SPECIAL PAGE FOR PEOPLE WHO ARE LOGGED IN')
