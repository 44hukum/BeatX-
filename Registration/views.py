from django.urls import path
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .beat_authentication import beat_user_authentication
from .beatauth import Authorize_Beat_User
from .delete import DeleteUser
#function based views

def index(request):
    try:
        if request.session.has_key('beatX_user'):
            return redirect('BeatXMusic:index')
        else:
            return render(request,'Registration/login.html')
    except:
        return render(request,'Registration/login.html')

 #views for login request
 #validate the user to authorize the user in beatx login function calls beatauth
def login(request):
    try:
        if request.method=="POST":
            auth=Authorize_Beat_User()
            userrAuth=auth.authorize(request.POST['username'],request.POST['password'])
            if userrAuth[0]:
                request.session['beatX_user']=userrAuth[1]
                return redirect('Registration:index')
            else:
                return render(request,'Registration/login.html',{'message': userrAuth[1]})
        else:
            return render(request,'Registration/login.html')
    except:
        return render(request,'Registration/login.html')
#views for signup
def signup(request):
    if request.method == "POST":
       #calls the create python file form the Registration app to create a user account
       #1: create functionality of CRUD operation
        if request.POST['password'] == request.POST['password2']: #conforms the password
             user=request.POST['username']
             email=request.POST['emailaddr']
             phone=request.POST['phone_number']
             gender=request.POST.get('gender','others')
             passw=request.POST['password'] #password hashing still remaining
             #validating user email and the phone number to see wether the provided information matches the database or not
             auth=beat_user_authentication()
             #if the user passes the validation process it calls the create
             #module to create the user account
             userrAuth=auth.validator(user,email,phone,gender,passw)
             if userrAuth[0]: #if the user creation is successfull
                request.session['beatX_user']=userrAuth[1]
                return redirect('Registration:index')
             else:
                 return render(request,'Registration/signup.html',{'message': userrAuth[1]})
        else:
            return render(request,'Registration/signup.html',{'message': 'password validation error'})
    else:
         return render(request,'Registration/signup.html')
#when the user forget the password it provides the functionality to update the password
def forgetpass(request):
    return render(request,'Registration/forget.html')

#deletes the session created
def logout(request):
    try:
        del request.session['beatX_user']
    except KeyError:
        pass
    finally:
        return redirect('Registration:index')

#delete the user and all the related assets with it
def deleteUser(request):
    userdelet=(DeleteUser().deleteuser(request.session['beatX_user']))
    if userdelet:
        return redirect('Registration:logout')
