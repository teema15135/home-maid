from datetime import date
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient

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

    @patch('maids.views.Maid')
    def test_mock_orm_1(self, mock):
        class MyObject:
            pass

        first = MyObject()
        first.name = "A"

        second = MyObject()
        second.name = "C"

        mock.objects.all.return_value = [
            first,
            second,
        ]

        response = self.client.get(reverse('maid-another-list'))

        assert '<li>A</li>' in str(response.content)
        assert '<li>C</li>' in str(response.content)

    @patch('maids.views.Maid.objects.all')
    def test_mock_orm_1(self, mock):
        class MyObject:
            pass

        first = MyObject()
        first.name = "A"

        second = MyObject()
        second.name = "C"

        mock.return_value = [
            first,
            second,
        ]

        response = self.client.get(reverse('maid-another-list'))

        assert '<li>A</li>' in str(response.content)
        assert '<li>C</li>' in str(response.content)

class TestMaidAddView(TestCase):
    def test_view_should_respond_200(self):
        response = self.client.get(reverse('maid-add'))
        assert response.status_code == 200

    def test_view_should_have_maid_form(self):
        response = self.client.get(reverse('maid-add'))

        print(str(response.content))
        assert '<form action="." method="POST">' in str(response.content)
        assert '<input type="text" name="name" maxlength="300" required id="id_name">' in str(response.content)
        assert '<button class="btn btn-primary" type="submit">Submit</button>' in str(response.content)
        assert '<input type="hidden" name="csrfmiddlewaretoken"' in str(response.content)

    def test_submit_form_should_save_new_maid(self):
        data = {
            'name': 'C'
        }
        self.client.post(reverse('maid-add'), data=data)

        maid = Maid.objects.last()

        assert maid.name == 'C'

    @patch('maids.views.send_mail')
    def test_after_submit_form_email_should_be_sent(self, mock):
        data = {
            'name': 'C'
        }
        self.client.post(reverse('maid-add'), data=data)

        mock.assert_called_once_with('Subject here'
                                    , 'Here is the message'
                                    , 'from@example.com'
                                    , ['to@example.com']
                                    , fail_silently=False
                                    )

class TestMaidAPIView(TestCase):
    def test_api_view_should_return_200(self):
        client = APIClient()
        response = client.get(reverse('maid-list-api'))
        assert response.status_code == 200