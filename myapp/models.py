from django.db import models

# Create your models here.

class IndexxParagraf(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    header = models.TextField(("Paragraf"))
    text = models.TextField(("Ana yazı"))
    user = models.CharField(("Kullanıcı Adı"), max_length=50)
    date_now = models.DateTimeField(("Paylaşım zamanı"),auto_now_add=False)
    image = models.FileField(("Kullanıcı Profil Fotoğrafı"), upload_to=None, max_length=100)