from django.contrib import admin
from .models import Server, Camera

# Register your models here.

admin.site.register(Camera)
admin.site.register(Server)

