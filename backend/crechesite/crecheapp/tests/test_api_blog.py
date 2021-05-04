import json
import os
import io

from PIL import Image
from django.conf import settings

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from crecheapp.models import Blog
from crecheapp.serializer import BlogSerializer


class BlogTestCase(APITestCase):
    def generate_photo_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_registration(self):
        user = User.objects.create(
            first_name="Bob",
            last_name="Green",
            username="bob@green.com",
            email="bob@green.com",
            is_active=True,
            is_staff=False)
        user.set_password('demo1234')
        user.save()

        data = {
            "titre": "Hello world",
            "description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry",
            "image": self.generate_photo_file(),
            "auteur": user
        }

        response = self.client.post("/api/blog/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_liste_blog(self):
        response = self.client.get("/api/blog/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)