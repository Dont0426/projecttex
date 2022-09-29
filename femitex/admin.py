from django.contrib import admin
from .models import Post, Profile

admin.site.register([Post, Profile])

# Register your models here.
