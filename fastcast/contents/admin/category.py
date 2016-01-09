from django.contrib import admin

from contents.models import Category


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = admin.ModelAdmin.list_display + (
        'name',
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    inlines = (
    )

    search_fields = (
        'name',
    )

    readonly_fields = (
    )
