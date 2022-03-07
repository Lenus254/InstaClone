from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/')
    bio = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.user.username}'
    
class Post(models.Model):
    pic = models.ImageField(upload_to = 'images/')
    caption = models.CharField(blank=True,max_length = 200)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.profile.user.username}'
    
class Comments(models.Model):
    post = models.IntegerField(default=0)
    username = models.CharField(blank=True,max_length = 100)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username}'
    
    
class Following(models.Model):
    username = models.CharField(blank=True,max_length = 100)
    followed = models.CharField(blank=True,max_length = 200)

    def __str__(self):
        return f'{self.username}'
