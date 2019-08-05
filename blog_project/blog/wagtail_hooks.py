from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import Product

class ProductAdmin(ModelAdmin):
    model = Product
    menu_label = 'Product'
    menu_icon = 'pilcrow'
    menu_order = 200

modeladmin_register(ProductAdmin)
