from django.contrib import admin
from.models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name' ,)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'category', 'is_active']
    list_filter = ['is_active', 'category'] 
    prepopulated_fields = {'slug': ('name',)}

    # method to display category name in list_display
    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'Category'
