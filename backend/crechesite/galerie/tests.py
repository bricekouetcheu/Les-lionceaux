from utilisateurs.tests import TestCase, BASE64_TEST_PICTURE
from galerie.models import Galerie
from galerie.serializers import GalerieSerializer

from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.six import BytesIO


class GalerieTestCase(TestCase):
    def test_galerie_serializer(self):
        """
        Test the galerie model serializer by serializing
        and deserializing an galerie object.
        """

        galerie = Galerie.objects.first()

        # Serialize galerie object
        serializer = GalerieSerializer(instance=galerie)

        # Deserialize galerie serialized data
        data = serializer.data
        image = BytesIO()
        Image.new("RGB", (100, 100)).save(image, "JPEG")
        image.seek(0)

        data["image"] = SimpleUploadedFile("image.jpg", image.getvalue())

        new_serializer = GalerieSerializer(data=data)
        if not new_serializer.is_valid():
            print(new_serializer.errors)
        self.assertTrue(new_serializer.is_valid())
        new_galerie = new_serializer.save()

        # Checking if each attribute value is identical
        for attr in (
            "titre",
            "album",
            "status",
        ):
            self.assertEqual(getattr(galerie, attr), getattr(new_galerie, attr))

    def test_get_all_galeries(self):
        """
        Test the enpoint to get all galeries
        """
        response = self.client.get("/api/galerie/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.get("count"),
            Galerie.objects.all().count(),
        )