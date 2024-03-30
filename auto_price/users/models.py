from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to=f"users_avatars", null=True, blank=True, verbose_name="Аватар"
    )
    phone_number = models.CharField(
        max_length=11, null=True, blank=True, verbose_name="Номер телефона"
    )


    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
