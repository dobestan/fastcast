import os
import random

from django.conf import settings
from django.core.management.base import BaseCommand

from contents.models import Content, Page

from faker import Factory


class Command(BaseCommand):
    help = "Install Pages fixture(s) in the database."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        # This is not recommended for loading fixtures.
        # In Real-life, should use django built-in loaddata fixtures feature.

        fake = Factory.create('ko_KR')

        # Delete Existing Pages
        Page.objects.all().delete()

        for content in Content.objects.all():
            random_page_count = random.randint(10, 50)
            for i in range(random_page_count):
                page = content.page_set.create(
                    description=fake.text(),
                )

            self.stdout.write("Successfully created {page_count} pages on content <{content_name}>".format(
                page_count=content.page_set.count(),
                content_name=content.title,
            ))
