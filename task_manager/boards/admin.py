from django.contrib import admin
from .models import Board, Column, Task


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created_at', 'updated_at')
    search_fields = ('name', 'owner__username')
    list_filter = ('created_at', 'updated_at')
    filter_horizontal = ('members',)


@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'board', 'position')
    search_fields = ('name', 'board__name')
    list_filter = ('board',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'column', 'assigned_to', 'due_date', 'created_at', 'updated_at')
    search_fields = ('title', 'column__name', 'assigned_to__username')
    list_filter = ('due_date', 'created_at', 'updated_at')
