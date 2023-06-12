from telnetlib import LOGOUT
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login
import authentication
from bpcl import settings

# Create your views here.
def home(request):
    return  render(request, 'authentication/index.html')


def signup(request):

    if request.method == 'post':
        # sname=request.post['sname']
        # email = request.post['email']
        # phone = request.post['phone']
        # password = request.post['password']
        # password1 = request.post['password1']

        # if User.objects.filter(email=email):
        #     messages.error(request, 'This email is already taken')
        #     return redirect('home')

        # if password != password1:
        #     messages.error(request,'Password dint matched!')


        # myuser = User.objects.create_user(email,password)
        # myuser.name = sname

        # myuser.save()

        messages.success(request, 'Your account is successfully created')

        return redirect('signin')


    return render(request, 'authentication/signup.html')

def signin(request):
    if request.method == 'post':
        email = request.post['email']
        password = request.post['password']

        user = authenticate(email = email, password = password)

        if user  is not None:
            login(request,user)
            sname = user.sname
            return render(request, 'authenticate/index.html',{'name': sname })

        else:
            messages.error(request, 'bad credintials !!!')
            return redirect('home')


    return render(request, 'authentication/signin.html')


def signout(request):
    LOGOUT(request)
    messages.success(request, 'logged out successfully')
    return redirect('home')

 

