from datetime import date

from django.test import TestCase

from ..models import Maid
from ..serializer import MaidSerializer

class TestMaidSerializer(TestCase):
    def test_serializer_should_serialize_object_to_json(self):
        # Given
        Maid.objects.create(
            name='A',
            birthdate=date(1998, 1, 1),
            description='Super Maid of the Year',
            certificate='Best Maid 2012',
            salary=3000
        )

        Maid.objects.create(
            name='C',
            birthdate=date(1998, 1, 2),
            description='Ultra Maid of the Year',
            certificate='Best Maid 2020',
            salary=3200
        )

        # When
        maids = Maid.objects.all()
        serializer = MaidSerializer(maids, many=True)

        # Then
        assert serializer.data == [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'C'}]