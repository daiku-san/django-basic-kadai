from django.contrib import admin
from .models import Product

# ProductAdminクラスを定義して、adminサイトでの表示方法をカスタマイズ
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

admin.site.register(Product, ProductAdmin)

# superuser INFO↓
# s
# qawsed08013290279
