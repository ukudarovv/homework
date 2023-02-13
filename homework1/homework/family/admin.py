from django.contrib import admin
from .models import *


class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(Child, ChildAdmin)


class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(Parent, ParentAdmin)
