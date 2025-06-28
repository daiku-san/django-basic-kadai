from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe
from django.contrib.humanize.templatetags.humanize import intcomma   # ★

admin.site.site_header = 'Admin site'
admin.site.site_title = 'Adminカスタムサイト管理'
admin.site.index_title = 'Admin管理者ページ'


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price_with_commas', 
        'category',
        'description',
        'thumbnail', # 画像サムネイルを表示
    )
    search_fields = ('name',)

    # 価格をカンマ区切り + 「円」付きで返す
    def price_with_commas(self, obj):
        return f'{intcomma(obj.price)} 円'
    price_with_commas.short_description = '価格'     # 列ヘッダ
    price_with_commas.admin_order_field = 'price'   # ソート対象列を price に

    # 画像サムネイル
    def thumbnail(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" style="width:100px;height:auto;" />')
        return "No Image"
    thumbnail.short_description = "Image"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


# from django.contrib import admin
# from .models import Product, Category
# from django.utils.safestring import mark_safe

# # 基本設定
# admin.site.site_header = 'Admin site'
# admin.site.site_title = 'Adminカスタムサイト管理'
# admin.site.index_title = 'Admin管理者ページ'

# # ProductAdminクラスを定義して、adminサイトでの表示方法をカスタマイズ
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'category', 'description', 'image')
#     search_fields = ('name',)

#     def image(self, obj):
#         if obj.img:
#             return mark_safe(f'<img src="{obj.img.url}" style="width: 100px; height: auto;" />')
#         return "No Image"
#     image.short_description = "Image"


# # CategoryAdminクラスを定義して、adminサイトでの表示方法をカスタマイズ
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')
#     search_fields = ('name',)

# admin.site.register(Product, ProductAdmin)
# admin.site.register(Category, CategoryAdmin)

# # superuser INFO↓
# # s
# # qawsed08013290279
