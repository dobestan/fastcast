from django.contrib import admin

from contents.models import Comment


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'page',
        'user',

        'content',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
        'content',

        'page__content__title',
        'page__content__subtitle',
    )

    readonly_fields = (
        'page',
        'user',
    )
