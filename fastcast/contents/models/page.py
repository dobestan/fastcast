from django.db import models


class PageManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'content',
            'content__category',
        )


class Page(models.Model):

    content = models.ForeignKey('Content')

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='설명',
    )

    # "*-cast" services is based on medias ( including images, videos ).
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='이미지',
    )
    image_source_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='이미지 출처 이름'
    )
    image_source_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='이미지 출처 URL'
    )

    class Meta:
        verbose_name = '컨텐츠 세부 페이지'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{content_title} - {description}".format(
            content_title=self.content.title,
            description=self.description,
        )
