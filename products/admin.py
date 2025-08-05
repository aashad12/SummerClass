from django.contrib import admin
from . models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
class ProductAdmin(admin.ModelAdmin):
    exclude =('created_at',)
    list_display = ('id','name', 'category','price','stock','status')    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)