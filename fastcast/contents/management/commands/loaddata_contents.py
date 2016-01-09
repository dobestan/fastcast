import os
import random

from django.conf import settings
from django.core.management.base import BaseCommand

from contents.models import Category, Content

from selenium import webdriver


class Command(BaseCommand):
    help = "Install Contents fixture(s) in the database."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        # This is not recommended for loading fixtures.
        # In Real-life, should use django built-in loaddata fixtures feature.

        # FIXME: Pikicast is not loading contents on PhantomJS.
        driver = webdriver.Firefox()
        driver.get("https://www.pikicast.com/")
        driver.implicitly_wait(10)

        category_elements = driver.find_elements_by_css_selector('ul.sub-cate > li')

        # Delete Existing Category, Content
        Category.objects.all().delete()

        for category_element in category_elements:
            category_link = category_element.find_element_by_css_selector('a').get_attribute('href')
            title = category_element.find_element_by_css_selector('a').get_attribute('text')

            # 카테고리 인스턴스 생성
            category, category_created= Category.objects.get_or_create(
                name=title,
            )

            self.stdout.write("{category_name}".format(
                category_name=category.name,
            ))

            # 카테고리 상세 페이지로 접속해서
            # 컨텐츠를 크롤링하여 컨텐츠 인스턴스 생성

            driver.get(category_link)
            content_elements = driver.find_elements_by_css_selector('div.thumnail-area ul.thumnail-list div.inner')

            for content_element in content_elements:
                # 피키캐스트의 경우에는 2가지 모양의 썸네일이 있다.
                # 하나가 파싱하는 과정에서 실패하면, 다른 css selector 로 시도해서 파싱하기
                # FIXME: This process is quite a bit slow.
                try:
                    title = content_element.find_element_by_css_selector('span.in').get_attribute('innerHTML').replace('<br>', ' ').replace('\n', '')
                except:
                    title = content_element.find_element_by_css_selector('span.tit').get_attribute('innerHTML').replace('<br>', ' ').replace('\n', '')

                content, content_created = category.content_set.get_or_create(
                    title=title,
                )

                # 컨텐츠 인스턴스를 업데이트
                # 가정: 한 플랫폼에서 많이 공유되는 컨텐츠는 다른 플랫폼에서도 많이 공유될 것이다.

                default_share_count = random.randint(10, 1000)

                content.kakaotalk_share_count = default_share_count + random.randint(-10, 70)
                content.facebook_share_count = default_share_count + random.randint(-10, 200)
                content.kakaostory_share_count = default_share_count + random.randint(-10, 70)
                content.line_share_count = default_share_count + random.randint(-10, 30)
                content.save()

                self.stdout.write("{category_name}, {content_title}".format(
                    category_name=category.name,
                    content_title=content.title,
                ))

        driver.quit()

        # Result Message
        self.stdout.write("Successfully created {category_count} categories, and {content_count} contents.".format(
            category_count=Category.objects.count(),
            content_count=Content.objects.count(),
        ))
