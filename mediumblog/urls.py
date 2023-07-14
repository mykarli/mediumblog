"""mediumblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *


app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexx, name='indexx'),
    path('getstarted/',getstarted, name='getstarted'),
    path('joinmedium/',joinmedium, name='joinmedium'),
    path('membership/',membership, name='membership'),
    path('ourstory/',ourstory, name='ourstory'),
    path('signin/',signin, name='signin'),
    path('write/',write, name='write'),
    path('welcome/',welcome, name='welcome'),
    path('post/',post, name='post'),
    path('postlike/',postlike,name='postlike'),
    
    
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
