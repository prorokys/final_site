from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError
from django.db import transaction
from django.shortcuts import redirect, render

from carts.models import Cart
from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem


@login_required
def create_order(request):

    if request.method == "POST":
        form = CreateOrderForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    # Зробити заказ
                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data["phone_number"],
                            required_delivery=form.cleaned_data["required_delivery"],
                            delivery_address=form.cleaned_data["delivery_address"],
                            payment_on_get=form.cleaned_data["payment_on_get"],
                        )

                        # Створити замовлення
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            quantity = cart_item.quantity
                            price = cart_item.product.sell_price()

                            if product.quantity < quantity:
                                raise ValidationError(
                                    f"Недостатня кількість товару {name} на складі\n"
                                    f"В наячності товару {name} на складі {product.quantity} шт."
                                )

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                quantity=quantity,
                                price=price,
                            )

                            product.quantity -= quantity
                            product.save()

                        # Очистити кошик після створення замовлення
                        cart_items.delete()

                        messages.success(request, "Замовлення сформовано!")
                        return redirect("user:profile")

            except ValidationError as e:

                messages.success(request, str(e))
                return redirect("cart:order")

    else:
        initial = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
        }

        form = CreateOrderForm(initial=initial)

    context = {
        "title": "Home - Створити замовлення",
        "form": form,
        "order": True,
    }

    return render(request, "orders/create_order.html", context=context)
