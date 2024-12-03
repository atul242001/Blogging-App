from django.contrib import admin
from .models import Category, Post
from django.utils.html import mark_safe

# Register your models here.

# For configuration of category admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)
    list_per_page = 50

    def image_tag(self, obj):
        if obj.image:  
            return mark_safe(f'<img src="{obj.image.url}" style="width:40px;height:40px;border-radius:50%;" />')
        return "No Image"

    image_tag.short_description = 'Image'


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','url', 'add_date')
    search_fields = ('title',)  
    list_filter = ('cat',)
    list_per_page = 50

    def image_tag(self, obj):
        if obj.image:  
            return mark_safe(f'<img src="{obj.image.url}" style="width:40px;height:40px;border-radius:50%;" />')
        return "No Image"

    image_tag.short_description = 'Image'  


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

