from django.contrib import admin
from .models import *

class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'department',
    )
    list_filter = (
        'department',
    )

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'group',
        'department',
        'average',
        'status',
        'get_grants',
    )
    list_filter = (
        'group',
        'department',
    )
    ordering = (
        'average',
        'name',
    )

class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'professor',
    )
    list_filter = (
        'professor',
    )

class MarkAdmin(admin.ModelAdmin):
    list_display = (
        'value', 
        'subject', 
        'student',
    )
    list_filter = (
        'subject', 
        'student',
    )

admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Mark, MarkAdmin)