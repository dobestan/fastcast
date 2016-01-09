from django.contrib import admin

from contents.models import Page


@admin.register(Page)
class PageModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'content',

        'description',
        'image',
        'image_source_name',
        'image_source_url',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
        'content__title',
        'content__subtitle',
    )

    readonly_fields = (
    )
