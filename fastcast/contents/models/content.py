from django.conf import settings
from django.db import models


class ContentManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'category',
        )


class Content(models.Model):

    category = models.ForeignKey('Category')

    title = models.CharField(
        max_length=128,
        verbose_name='제목',
    )
    subtitle = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='부제목',
    )

    # Share Count
    kakaotalk_share_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='카카오톡 공유 횟수',
    )
    facebook_share_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='페이스북 공유 횟수',
    )
    kakaostory_share_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='카카오스토리 공유 횟수',
    )
    line_share_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name='라인 공유 횟수',
    )

    # Like
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='content_like_set',
    )

    objects = ContentManager()

    class Meta:
        verbose_name = '컨텐츠'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
