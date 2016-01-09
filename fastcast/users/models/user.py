from django.db import models
from django.contrib.auth.models import UserManager as DefaultUserManager, AbstractUser


class UserManager(DefaultUserManager):
    pass


class User(AbstractUser):

    name = models.CharField(
        max_length=8,
        verbose_name='이름',
    )

    address = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='주소지',
    )

    is_editor = models.BooleanField(
        default=False,
        verbose_name='에디터',
    )

    objects = UserManager()

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
