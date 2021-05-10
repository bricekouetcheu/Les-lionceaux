
import io

from PIL import Image

from rest_framework import status
from rest_framework.test import APITestCase

from crecheapp.models import Galerie, Album


class GalerieTestCase(APITestCase):
    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_registration(self):
        album = Album.objects.create(titre="Bob", )
        data = {
            "album": album,
            "titre": "Hello world",
            "image": self.generate_photo_file()
        }

        response = self.client.post("/api/galerie/", data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_liste_galerie(self):
        response = self.client.get("/api/galerie/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


