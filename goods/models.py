from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="назва")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "категорію"
        verbose_name_plural = "категорії"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="назва")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="опис")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="зображення"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="ціна", default=0.00
    )
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="скидка в %", default=0.00
    )
    quantity = models.PositiveIntegerField(verbose_name="кількість", default=0)
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="категорія"
    )

    class Meta:
        db_table = "product"
        verbose_name = "продукт"
        verbose_name_plural = "продукти"
        ordering = ("id",)

    def __str__(self):
        return f"{self.name} Кількість- {self.quantity}, {self.image}"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
