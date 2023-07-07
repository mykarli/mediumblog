from django.shortcuts import render ,redirect
from.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def indexx(request):
    indexxparagraf = IndexxParagraf.objects.all()
    
    context={
        "indexxparagraf":indexxparagraf
        
    }
    
    return render(request,'indexx.html',context)


def getstarted(request):

    
    context={
        
    }
    
    return render(request,'getstarted.html',context)

def joinmedium(request):

    
    context={
        
    }
    
    return render(request,'joinmedium.html',context)

def membership(request):

    
    context={
        
    }
    
    return render(request,'membership.html',context)

def ourstory(request):

    
    context={
        
    }
    
    return render(request,'ourstory.html',context)

def signin(request):

    
    context={
        
    }
    
    return render(request,'signin.html',context)

def welcome(request):

    
    context={
        
    }
    
    return render(request,'welcome.html',context)

def write(request):

    
    context={
        
    }
    
    return render(request,'write.html',context)


def kayıtol(request):
    
    context={
        
    
    }
    if request.method == 'POST':
        
        name = request.POST["name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 == password2:
            if not User.objects.filter(username = email).exists():
                if not User.objects.filter(email = email).exists():
                    user = User.objects.create_user(first_name=name,usernaname=email,email=email,password=password1)
                    user.save()
                    userinfo = UserInfo(user = user , password = password1)
                    userinfo.save()
                    messages.success(request,"Kayıt Olma Başarılı")
                    return redirect()
                else:
                    messages.warning(request,"Bu mail üzerine daha önce bir kullanıcı oluşturulmuş.")
                    return redirect()
            else:
                messages.warning(request,"Bu kullanıcı adı üzerine daha önce bir kullanıcı oluşturulmuş.")
                return redirect()
            
        else:
            messages.warning(request,"Şifreyi doğru girdiğinden emin ol.")
            return redirect()
        
    return render(request,'indexx.html',context)
                