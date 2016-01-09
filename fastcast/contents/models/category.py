from django.db import models


class CategoryManager(models.Manager):
    pass


class Category(models.Model):

    name = models.CharField(
        max_length=64,
        unique=True,
    )

    objects = CategoryManager()

    class Meta:
        verbose_name = '카테고리'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
