from django.contrib import admin
#import post class from model 
from .models import Post
# Register pages models here.
admin.site.register(Post)


