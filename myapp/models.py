from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class IndexxParagraf(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    header = models.TextField(("Paragraf"))
    text = models.TextField(("Ana yazı"))
    user = models.CharField(("Kullanıcı Adı"), max_length=50)
    date_now = models.DateTimeField(("Paylaşım zamanı"),auto_now_add=False)
    image = models.FileField(("Kullanıcı Profil Fotoğrafı"), upload_to=None, max_length=100)
    

class UserInfo(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı adı"), on_delete=models.CASCADE)
    password = models.CharField(("Parola"), max_length=50)


class Post(models.Model):
    title = models.CharField(("Başlık"),max_length=200)
    content = models.TextField(("Paragraf"))
     