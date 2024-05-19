from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users_images", blank=True, null=True, verbose_name="Аватар"
    )

    class Meta:
        db_table = "user"
        verbose_name = "користувача"
        verbose_name_plural = "користувачи"

    def __str__(self):
        return self.username
