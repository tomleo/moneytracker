from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from . import models
from . import factories


class TestCategory(APITestCase):

    def setUp(self):
        self.password = 'asdf'
        self.user = factories.UserFactory.create()
        self.list_url = reverse('list-category')
        self.post_url = reverse('add-category')

    def test_add_category(self):
        self.client.login(username=self.user.username, password=self.password)
        data = {'name': 'Cats'}
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Category.objects.count(), 1)
        self.assertEqual(models.Category.objects.get(pk=response.data['id']).name, data['name'])

    def test_add_category_unauthenticated(self):
        data = {'name': 'Cats'}
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(models.Category.objects.count(), 0)

    def test_list_category(self):
        self.client.login(username=self.user.username, password=self.password)
        factories.CategoryFactory.create(name='Dogs')
        factories.CategoryFactory.create(name='Cats')
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 2)

    def test_list_category_empty(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 0)

    def test_list_category_unauthenticated(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestNote(APITestCase):

    def setUp(self):
        self.password = 'asdf'
        self.user = factories.UserFactory.create()
        self.list_url = reverse('list-note')
        self.post_url = reverse('add-note')

    def test_add_note(self):
        self.client.login(username=self.user.username, password=self.password)
        data = {'name': 'Run', 'description': '9 Mile Loop'}
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Note.objects.count(), 1)
        self.assertEqual(models.Note.objects.get(pk=response.data['id']).name, data['name'])

    def test_list_note_empty(self):
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Note.objects.count(), 0)

    def test_list_note(self):
        factories.NoteFactory.create()
        factories.NoteFactory.create()
        self.client.login(username=self.user.username, password=self.password)
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Note.objects.count(), 2)


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
