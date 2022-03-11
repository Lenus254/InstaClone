from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/',default='images/default.jpg', null=True)
    bio = models.CharField(max_length = 200)

    def __str__(self):
        return f'{self.user.username}'
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
    
class Post(models.Model):
    pic = models.ImageField(upload_to = 'images/',default='images/default.jpg' )
    caption = models.CharField(blank=True,max_length = 200)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.profile.user.username}'
    
    def save_post(self):
        self.save()
    
    @property
    def image_url(self):
        if self.pic and hasattr(self.pic, 'url'):
            return self.pic.url
    
class Comments(models.Model):
    post = models.IntegerField(default=0)
    username = models.CharField(blank=True,max_length = 100)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username}'
    
    def save_comment(self):
        self.save()
    
    
class Following(models.Model):
    username = models.CharField(blank=True,max_length = 100)
    followed = models.CharField(blank=True,max_length = 200)
    image = models.ImageField(upload_to = 'images/' )

    def __str__(self):
        return f'{self.username}'
    
    def save_follower(self):
        self.save()
