

from rest_framework import status
from rest_framework.test import APITestCase


class AlbumTestCase(APITestCase):

    def test_registration(self):
        data = {
            "titre": "Hello world",
        }

        response = self.client.post("/api/album/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_liste_album(self):
        response = self.client.get("/api/album/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
