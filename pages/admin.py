from django.contrib import admin
from . models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'content', 'created_at')    
admin.site.register(Page)



