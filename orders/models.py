from django.db import models

from goods.models import Products
from users.models import User


class OrderItemQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(models.Model):

    user = models.ForeignKey(
        to=User,
        on_delete=models.SET_DEFAULT,
        blank=True,
        null=True,
        verbose_name="Користувач",
        default=None,
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата створення замовлення"
    )
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефону")

    required_delivery = models.BooleanField(
        verbose_name="Потрібна доставка", default=False
    )
    delivery_address = models.TextField(
        blank=True, null=True, verbose_name="Адреса доставки"
    )
    payment_on_get = models.BooleanField(
        verbose_name="Оплата при отриманні", default=False
    )
    is_paid = models.BooleanField(verbose_name="Оплачено", default=False)
    status = models.CharField(
        max_length=50, verbose_name="Статус замовлення", default="У процесі"
    )

    class Meta:
        db_table = "order"
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"

    def __str__(self):
        return f"Замовлення № {self.pk} | Покупець {self.user.first_name} {self.user.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, verbose_name="Замовлення"
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.SET_DEFAULT,
        verbose_name="Товар",
        null=True,
        default=None,
    )
    name = models.CharField(max_length=150, verbose_name="Назва")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Ціна", default=0.00
    )
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Кількість")
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата продажу"
    )

    class Meta:
        db_table = "order_item"
        verbose_name = "Проданий товар"
        verbose_name_plural = "Продані товари"

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        return f"Товар {self.name} | Замовлення № {self.order.pk} "
