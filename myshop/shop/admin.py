from django.contrib import admin
from .models import Category, Product

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']

    '''
    list_editable attribute sets the fields that 
    can be edited from the list display page of the admin site. This allows
    to edit multiple rows at once. Any field in list_editable must also be listed 
    in the list_display attribute, since only the fields displayed can be edited.
    '''
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}