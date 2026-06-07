from django.contrib import admin
from recipes.models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(Recipe, RecipeAdmin)
