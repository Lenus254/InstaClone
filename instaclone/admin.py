from django.contrib import admin
from .models import Post, Profile, Comments, Following

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Following)



