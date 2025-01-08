from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):

    return render(request,'index.html')


def handleSignup(request):
    if request.method == 'POST':

        # TAKE THE PARAMETERS FROM THE POP UP FORM
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if len(username)>15:
            messages.error(request,"username should be less than 15 characters")
            return redirect('/')

            

        if not username.isalnum():
            return HttpResponse("usernames should contain only letters and numbers") 

        if pass1 != pass2:
            return HttpResponse("your password is incorrect")
            
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return redirect('/')
        

def handleLogin(request):

    if request.method == "POST":

        # GET PARAMETERS
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:

            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/')




