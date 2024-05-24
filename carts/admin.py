from django.contrib import admin
from carts.models import Cart

# Register your models here.
# admin.site.register(Cart)


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ["product", "quantity", "created_timestamp"]
    extra = 1
    readonly_fields = ("created_timestamp",)
    search_fields = ["product", "quantity", "created_timestamp"]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = ["user_display", "product_display", "quantity", "created_timestamp"]
    list_filter = ["user", "product__name", "created_timestamp"]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимний користувач"

    def product_display(self, obj):
        return str(obj.product.name)
