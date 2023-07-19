from django.contrib import admin
from .models import student,professor

# Register your models here.
admin.site.register(professor)
admin.site.register(student)