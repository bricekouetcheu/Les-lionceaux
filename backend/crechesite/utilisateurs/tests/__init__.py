from django.test import TestCase as DjangoTestCase


# This is a small tap logo in png format
BASE64_TEST_PICTURE = {
    "file": "data:image/png;base64,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",  # noqa:
    "name": "lionceaux.png",
}


class TestCase(DjangoTestCase):
    fixtures = [
        "utilisateur.json",
        "groupe.json",
        "enfant.json",
        "blog.json",
        "agenda.json",
        "album.json",
        "galerie.json",
        "activite.json",


    ]

    def setUp(self):
        pass