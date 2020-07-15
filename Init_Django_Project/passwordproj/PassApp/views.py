from django.shortcuts import render
from PassApp.forms import UserForm, UserProfileForm

# Create your views here.
def index(request):
    return render(request, 'passapp\index.html')

def register(request):
    registered = False
    if request.method == "POST":
        userform = UserForm(request.POST)

        profileform = UserProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()


            profile = profileform.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
            return index(request)
        else:
            print(user.errors, profile.errors)
    else:
        userform = UserForm()
        profileform = UserProfileForm()

    return render(request, 'passapp/register.html', context = {'registered': registered,
                                                                'form_user':userform,
                                                                'form_profile':profileform})
