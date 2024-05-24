from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabularAdmin
from users.models import User

# admin.site.register(User)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name", "username", "email")
    list_display = (
        "first_name",
        "last_name",
        "username",
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
    )

    inlines = [CartTabAdmin, OrderTabularAdmin]
