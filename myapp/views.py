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