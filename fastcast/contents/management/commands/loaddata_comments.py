import os
import random

from django.conf import settings
from django.core.management.base import BaseCommand

from contents.models import Page, Comment
from users.models import User

from faker import Factory


class Command(BaseCommand):
    help = "Install Comments fixture(s) in the database."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        # This is not recommended for loading fixtures.
        # In Real-life, should use django built-in loaddata fixtures feature.

        fake = Factory.create('ko_KR')

        # Delete Existing Comment
        Comment.objects.all().delete()

        # 모든 페이지에 댓글이 달리는 것은 아니며,
        # 하위 20% 를 제외한 페이지에 댓글이 달린다.
        for page in Page.objects.order_by('?')[:int(Page.objects.count() - Page.objects.count()/5)]:

            # 몇 개의 댓글이 달릴지 결정
            comments_count = random.randint(10, 60)

            # 댓글을 달아야하는 유저
            users = User.objects.all().order_by('?')[:comments_count]

            for user in users:
                page.comment_set.create(
                    user=user,
                    content=fake.text(),
                )

            self.stdout.write("Successfully created {comments_count} comments on page #{page_id}".format(
                comments_count=page.comment_set.count(),
                page_id=page.id,
            ))
