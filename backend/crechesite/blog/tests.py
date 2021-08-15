from utilisateurs.tests import TestCase, BASE64_TEST_PICTURE
from blog.models import Blog
from blog.serializers import BlogSerializer

from PIL import Image

from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.six import BytesIO


class BlogTestCase(TestCase):
    def test_blog_serializer(self):
        """
        Test the blog model serializer by serializing
        and deserializing an blog object.
        """

        blog = Blog.objects.first()

        # Serialize blog object
        serializer = BlogSerializer(instance=blog)

        # Deserialize blog serialized data
        data = serializer.data
        image = BytesIO()
        Image.new('RGB', (100, 100)).save(image, 'JPEG')
        image.seek(0)

        #data['image'] = SimpleUploadedFile('image.jpg', image.getvalue())

        new_serializer = BlogSerializer(data=data)
        if not new_serializer.is_valid():
            print(new_serializer.errors)
        self.assertTrue(new_serializer.is_valid())
        new_blog = new_serializer.save()

        # Checking if each attribute value is identical
        for attr in (
                "titre",
                "description",
                "auteur",
                "status",
        ):
            self.assertEqual(getattr(blog, attr), getattr(new_blog, attr))

    def test_get_all_blogs(self):
        """
        Test the enpoint to get all blogs
        """
        response = self.client.get("/api/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.get("count"),
            Blog.objects.all().count(),
        )