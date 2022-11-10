from django.contrib import admin
from store.models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name','price','stock','is_available','category','modified_date']
    prepopulated_fields = {"slug" : ("product_name",)}

