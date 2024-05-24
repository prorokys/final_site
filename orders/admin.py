from django.contrib import admin

from orders.models import Order, OrderItem


# admin.site.register(Order)
# admin.site.register(OrderItem)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "name", "price", "quantity")
    search_fields = ("order", "product", "name")


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = ["product", "name", "price", "quantity"]
    extra = 0
    search_fields = ["product", "name"]


class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = (
        "required_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    extra = 0
    search_fields = (
        "required_delivery",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "phone_number",
        "required_delivery",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    list_filter = (
        "status",
        "is_paid",
        "payment_on_get",
        "required_delivery",
    )
    search_fields = ("id",)
    readonly_fields = ("created_timestamp",)

    inlines = (OrderItemTabularAdmin,)
