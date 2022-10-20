from django.contrib import admin
from .models import Task

#para agregar campos de solo lectura al admin
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("created",)
# Register youmoder models here.
admin.site.register(Task,TaskAdmin)