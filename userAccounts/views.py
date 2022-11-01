from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.conf import settings
from .models import Profile
from .forms import UserRegistrationForm,UserProfileForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate
import random
import requests

def login(request):
    context={}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user:
            return redirect('/shops/showShops')
        else:
            context['message']="Incorrect Username or Password!"

    return render(request, 'shops/login.html',context)

def signup(request):
    return render(request, 'shops/signup.html')

def sendOTP(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    api = "api key here"
    querystring = {"authorization":api,"sender_id":"FSTSMS","message":message,"language":"english","route":"p","numbers":number}
    headers = {
        'cache-control': "no-cache"
    }
    return requests.request("GET", url, headers=headers, params=querystring)

def register(request):
    if request.method == 'POST':

        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        username = request.POST['username']

        usernameExist = User.objects.filter(username = username).first()
        emailExist = User.objects.filter(email = email).first()
        profileExist = Profile.objects.filter(phone_number = mobile).first()
        
        if usernameExist or profileExist or emailExist:
            context = {'message' : 'User already exists'}
            return render(request,'shops/signup.html' , context)

        request.session['email'] = email
        request.session['username'] = username
        request.session['password'] = password
        request.session['number'] = mobile

        otp = str(random.randint(1000 , 9999))
        request.session['otp'] = otp
        message = f'your otp is {otp}'
        #sendOTP(mobile,message)
        return redirect('/account/otp')

    return render(request, 'shops/signup.html')

def getotp(request):

    if request.method == "POST":
        u_otp = request.POST['otp']
        # otp = request.session.get('otp')
        otp=1234
        user = request.session['username']
        hash_pwd = make_password(request.session.get('password'))
        p_number = request.session.get('number')
        email_address = request.session.get('email') 

        if int(u_otp) == otp:
            User.objects.create(
                            username = user,
                            email=email_address,
                            password=hash_pwd
            )
            user_instance = User.objects.get(username=user)
            Profile.objects.create(
                            user = user_instance,phone_number=p_number
            )
            request.session.delete('otp')
            request.session.delete('user')
            request.session.delete('email')
            request.session.delete('password')
            request.session.delete('phone_number')

            # messages.success(request,'Registration Successfully Done !!')
            return redirect('/account/login')
        
    return render(request,'shops/otp.html')