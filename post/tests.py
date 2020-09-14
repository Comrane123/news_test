from rest_framework.test import APITestCase, APIClient
from .models import Post


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_post(title="", url=""):
        if title != "" and url != "":
            Post.objects.create(title=title, url=url)

    def setUp(self):
        # add test data
        self.create_post(
            "Post 1",
            "https://24tv.ua/nova-zustrich-normandskomu-formati-yermak-nazvav-zavdannya_n1415051",
        )
        self.create_post(
            "Post 2",
            "https://socportal.info/ru/news/ukraina-razreshila-vezd-eshche-odnoi-gruppe-inostrantcev/",
        )
        self.create_post(
            "Post 3",
            "https://www.rbc.ua/rus/news/ukraine-sobirayutsya-uregulirovat-polozheniya-1600110230.html",
        )
        self.create_post("Post 4", "https://www.radiosvoboda.org/a/30838635.html")
