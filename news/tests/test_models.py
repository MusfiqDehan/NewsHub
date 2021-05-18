from django.test import TestCase
from news.models import News


class TestModels(TestCase):

    def test_news(self):
        news = News()

        news.headline = "Israel Gaza conflict: Netanyahu vows to continue strikes"
        news.original_link = "https://www.bbc.com/news/world-middle-east-57131272"
        news.img_link = "https://ichef.bbci.co.uk/news/976/cpsprodpb/9F76/production/_118522804_gazabbc.jpg"
        news.newspaper_name = "BBC News"

        news.save()

        record = News.objects.get(pk=1)
        self.assertEqual(record, news)