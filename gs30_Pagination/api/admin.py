from django.contrib import admin
from api.models import Student

# Register your models here.

@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll' ]
