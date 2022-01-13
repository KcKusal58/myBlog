from django.db import models
from django.urls import reverse
#from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_desc = models.CharField(max_length=300, default="")
    author = models.CharField(max_length=20, default="Kushal KC")
    slug = models.CharField(max_length=100)
    #publisher = models.ForeignKey(User , on_delete=models.CASCADE)

    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-slug', kwargs={'slug': self.slug})
    

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    desc =models.TextField()
    time = models.DateTimeField(auto_now_add=True)