from django.contrib import admin

from contents.models import Content


@admin.register(Content)
class ContentModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'title',
        'subtitle',

        'category',

        'kakaotalk_share_count',
        'facebook_share_count',
        'kakaostory_share_count',
        'line_share_count',
    )

    list_filter = admin.ModelAdmin.list_filter + (
        'category',
    )

    inlines = (
    )

    search_fields = (
        'title',
        'subtitle',
    )

    readonly_fields = (
    )
