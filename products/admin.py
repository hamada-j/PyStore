from django.contrib import admin
from .models import Product, Offert


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OffertAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin)

admin.site.register(Offert, OffertAdmin)
