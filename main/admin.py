from django.contrib import admin
from .models import *

# from django.contrib.admin.models import LogEntry

from django.contrib.auth.models import User, Group as UserGroup
# from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(UserGroup)

# LogEntry.objects.all().delete()

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
        'status',
        'get_grants',
    )
    ordering = (
        'average',
        'name',
    )
    readonly_fields = (
	    'average',
	    'department',
	    'status',
	    'get_grants',
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
# admin.site.register(StudentStatus)
# admin.site.register(StudentGetGrants)
