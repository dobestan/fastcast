from django.conf import settings
from django.db import models


class CommentManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'page',
            'page__content',

            'user',
        )


class Comment(models.Model):

    page = models.ForeignKey('Page')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        verbose_name='상위 댓글',
    )

    content = models.TextField(
        verbose_name='내용'
    )

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='comment_like_set',
    )

    objects = CommentManager()

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "<{user_name} commented on {content_name}>".format(
            user_name=self.user.name,
            content_name=self.page.content.title,
        )
