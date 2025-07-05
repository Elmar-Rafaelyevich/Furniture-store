from django.contrib import admin
from goods.models import Categories, Products




@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    '''Автоматически будет заполняться поле slug, значение для slug га будет браться по поле name'''
    prepopulated_fields = {'slug':('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    '''Автоматически будет заполняться поле slug, значение для slug га будет браться по поле name'''

    prepopulated_fields = {'slug':('name',)}

    