from django.contrib import admin

# Register your models here.

from rango.models import Category, Page

# class PageInline(admin.TabularInline):
#     model = Page
#     extra = 0

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    # list_display = ('name', 'views', 'likes')
    # #list_filter = ['views'] # to enable selecting just categories with X number of views
    # search_fields = ['name']
    # fieldsets = [
    #     (None, {'fields': ['name']}),
    #     ('Statistics', {'fields': ['views', 'likes']}),
    #     ]
    # inlines = [PageInline] # table of pages associated with this category

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)