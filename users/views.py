from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import UserProfile

def login(request):
    if request.user.is_authenticated:
        return redirect('/userprofile')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active==True:
            auth_login(request, user)
            return redirect('/userprofile')
            
        else:
            return render(request, 'base.html', {"invalid_login": True})

     # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        existing_users = User.objects.filter(username=username)
        if existing_users:
            return render(request, '400.html', {"user_exists":"User already Exists"})

        try:
            new_user = User.objects.create(email='email', username=username)
        except:
            return render(request, '400.html', {"incorrect_email": "Incorrect Email"})
        new_user.set_password(password)
        new_user.save()
        UserProfile.objects.create(user=new_user)
        return redirect('/login')
    return render(request, 'register.html')

@login_required
def userprofile(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(request.user)
        if request.method == 'POST':
            profile.first_name = request.POST.get('first_name', '') 
            profile.last_name = request.POST.get('last_name', '') 
            profile.profile_picture = request.POST.get('profile_picture', '') 
            profile.i_can = request.POST.get('i_can', '') 
            profile.i_need = request.POST.get('i_need', '')
            profile.save()

    ctx = {"first_name":profile.first_name, "last_name":profile.last_name, "profile_picture":profile.profile_picture, 
                "i_can":profile.i_can, "i_need":profile.i_need, "verified":profile.verified}
    return render(request, 'userprofile.html', context=ctx)

