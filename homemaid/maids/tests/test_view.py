from datetime import date

from django.test import TestCase
from django.urls import reverse

from ..models import Maid


class TestMaidListView(TestCase):
    def test_view_should_respond_200(self):
        # reverse use to convert maid-list to url
        response = self.client.get(reverse('maid-list'))
        assert response.status_code == 200

    def test_view_should_display_maid_list(self):
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
        response = self.client.get(reverse('maid-list'))

        # Then
        assert '<li>A</li>' in str(response.content)
        assert '<li>C</li>' in str(response.content)

class TestMaidListAnotherView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-another-list'))
        assert response.status_code == 200

    def test_view_should_display_maid_list(self):
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
        response = self.client.get(reverse('maid-another-list'))

        # Then
        assert '<li>A</li>' in str(response.content)
        assert '<li>C</li>' in str(response.content)