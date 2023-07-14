from django.shortcuts import render ,redirect
from.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import PostForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.


def indexx(request):
    indexxparagraf = IndexxParagraf.objects.all()
    
    context={
        "indexxparagraf":indexxparagraf
        
    }
    if request.POST.get('submit') == 'register':
        if request.method == 'POST':
            
            name = request.POST["name"]
            email = request.POST["email"]
            password1 = request.POST["password1"]
            password2 = request.POST["password2"]
            
            if password1 == password2:
                if not User.objects.filter(username = email).exists():
                    if not User.objects.filter(email = email).exists():
                        user = User.objects.create_user(username=email, first_name=name,email=email,password=password1)
                        user.save()
                        userinfo = UserInfo(user = user , password = password1)
                        userinfo.save()
                        messages.success(request,"Kayıt Olma Başarılı")
                        return redirect('indexx')
                    else:
                        messages.warning(request,"Bu mail üzerine daha önce bir kullanıcı oluşturulmuş.")
                        return redirect('indexx')
                else:
                    messages.warning(request,"Bu kullanıcı adı üzerine daha önce bir kullanıcı oluşturulmuş.")
                    return redirect('indexx')
                
            else:
                messages.warning(request,"Şifreyi doğru girdiğinden emin ol.")
                return redirect('indexx')
    
    if request.POST.get('submit') == 'login':
        
        if request.method == 'POST':
            username = request.POST["email"]
            password = request.POST["password"]
            
            user = authenticate(request, username = username, password = password)
            
            if User is not None:
                login(request,user)
                messages.success(request,"Giriş yapıldı")
                return redirect('signin')
            else:
                messages.warning(request, "kullanıcı adı veya şifre hatalı")
                return redirect('indexx')
            
            
            

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



def post(request):
    likedposts = Post.objects.all() 
    context={
        likedposts:'likedposts'
    
    }
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Gönderi listesine yönlendirme
    else:
        form= PostForm()
    return render(request,'post.html',{'form': form})


def postlike(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        
    else:
        post.likes.add(request.user)
    return redirect('postlike.html', post_id =post_id)        





    
            
    
    
   
        
    
                