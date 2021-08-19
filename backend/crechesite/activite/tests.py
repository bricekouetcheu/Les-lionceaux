from utilisateurs.tests import TestCase
from activite.models import Activite
from activite.serializers import ActiviteSerializer


class ActiviteTestCase(TestCase):
    def test_activite_serializer(self):
        """
        Test the activite model serializer by serializing
        and deserializing an activite object.
        """

        activite = Activite.objects.first()

        # Serialize Activite object
        serializer = ActiviteSerializer(instance=activite)

        # Deserialize activite serialized data
        data = serializer.data
        new_serializer = ActiviteSerializer(data=data)
        if not new_serializer.is_valid():
            print(new_serializer.errors)
        self.assertTrue(new_serializer.is_valid())
        new_activite = new_serializer.save()

        # Checking if each attribute value is identical
        for attr in (
            "date_activite",
            "heure_debut",
            "heure_fin",
            "art",
            "lecture",
            "remarque",
        ):
            self.assertEqual(getattr(activite, attr), getattr(new_activite, attr))

    def test_get_all_activites(self):
        """
        Test the enpoint to get all activites
        """
        response = self.client.get("/api/activite/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.get("count"),
            Activite.objects.all().count(),
        )

