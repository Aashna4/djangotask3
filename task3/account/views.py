from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from .models import profile

def signup(request):
    if request.method=='POST' :
        
        fname = request.POST['f_name']
        lname = request.POST['l_name']
        username = request.POST['user_name']
        email = request.POST['email_id']
        pass1 = request.POST['p1']
        pass2 = request.POST['p2']
        phno = request.POST['ph_no']

        if(pass1==pass2):
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username unavailable.')
                return render(request, 'account/signup.html')
            else:
                user = User.objects.create_user(username= username, first_name=fname, last_name=lname, email=email, password=pass1)
                userinfo = profile(phno=phno, user=user)
                userinfo.save()
                auth.login(request, user)
                messages.success(request, f'User {user.username} successfully logged in!')
                return render(request, 'account/logout.html')
        messages.error(request, 'Passwords do not match.')
        return render(request, 'account/signup.html')
    return render(request, 'account/signup.html')

def login(request):
    if request.method=="POST":
        username= request.POST['user_name']
        p = request.POST['p1']
        user = auth.authenticate(username=username, password=p)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'User {user.username} successfully logged in!')
            return render(request, 'account/logout.html')
        messages.error(request, 'Invalid Credentials.')
        return render(request, 'account/login.html')
    return render(request, 'account/login.html')


def logout(request) :
    auth.logout(request)
    messages.success(request, 'Successfully logged out! Sign up/Log in again.')
    return render(request, 'account/signup.html')
   