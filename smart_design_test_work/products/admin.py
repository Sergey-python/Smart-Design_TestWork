from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Product._meta.fields if field.name != 'id']

admin.site.register(Product, ProductAdmin)
