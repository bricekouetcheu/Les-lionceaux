from utilisateurs.tests import TestCase
from agenda.models import Agenda
from agenda.serializers import AgendaSerializer


class AgendaTestCase(TestCase):
    def test_agenda_serializer(self):
        """
        Test the agenda model serializer by serializing
        and deserializing an agenda object.
        """

        agenda = Agenda.objects.first()

        # Serialize agenda object
        serializer = AgendaSerializer(instance=agenda)

        # Deserialize agenda serialized data
        data = serializer.data
        new_serializer = AgendaSerializer(data=data)
        if not new_serializer.is_valid():
            print(new_serializer.errors)
        self.assertTrue(new_serializer.is_valid())
        new_agenda = new_serializer.save()

        # Checking if each attribute value is identical
        for attr in (
            "date_evenement",
            "heure",
            "titre_evenement",
            "description",
            "visible",
        ):
            self.assertEqual(getattr(agenda, attr), getattr(new_agenda, attr))

    def test_get_all_agendas(self):
        """
        Test the enpoint to get all agendas
        """
        response = self.client.get("/api/agenda/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data.get("count"),
            Agenda.objects.all().count(),
        )