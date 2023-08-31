from django.contrib import admin
from Tasks.models import ToDo


@admin.register(ToDo)
class ToDoadmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority','date')
