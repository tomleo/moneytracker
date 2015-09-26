from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from . import models
from . import factories


class TestCategory(APITestCase):

    def setUp(self):
        self.password = 'asdf'
        self.user = factories.UserFactory.create()

    def test_add_category(self):
        self.client.login(username=self.user.username, password=self.password)
        url = reverse('add-category')
        data = {'name': 'Cats'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Category.objects.count(), 1)
        self.assertEqual(models.Category.objects.get().name, 'Cats')

    def test_list_category(self):
        self.client.login(username=self.user.username, password=self.password)
        url = reverse('list-category')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 0)
        factories.CategoryFactory.create(name='Dogs')
        factories.CategoryFactory.create(name='Cats')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 2)


class TestNote(APITestCase):

    def test_add_note(self):
        pass

    def test_list_note(self):
        pass


class TestPlace(APITestCase):

    def test_add_place(self):
        pass

    def test_list_place(self):
        pass


class TestSpending(APITestCase):

    def test_add_spending(self):
        pass

    def test_list_spending(self):
        pass
