from django.contrib import admin
from .models import Category
from .models import Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
    
admin.site.register(Recipe, RecipeAdmin)