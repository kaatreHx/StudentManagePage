from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(StudentData)

class StudentDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'contact', 'semester', 'profilePic')
