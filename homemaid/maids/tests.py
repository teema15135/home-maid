from datetime import date

from django.test import TestCase

from .models import Maid


class TestMaid(TestCase):
    def test_model_should_have_defined_fields(self):
        # Given
        Maid.objects.create(
            name='A',
            birthdate=date(1998, 1, 1),
            description='Super Maid of the Year',
            certificate='Best Maid 2012',
            salary=3000
        )

        # When
        maid = Maid.objects.last()

        # Then
        self.assertEqual(maid.name, 'A')
        self.assertEqual(maid.birthdate, date(1998, 1, 1))
        self.assertEqual(maid.description, 'Super Maid of the Year');
        self.assertEqual(maid.certificate, 'Best Maid 2012')
        self.assertEqual(maid.salary, 3000)
