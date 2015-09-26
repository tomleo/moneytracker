from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from . import models
from . import factories


class BaseCaseMixin(object):

    def setUp(self):
        self.password = 'asdf'
        self.user = factories.UserFactory.create()
        self.list_url = self.get_list_url()
        self.post_url = self.get_post_url()

    def get_list_url(self):
        return reverse('list-' + self.url_postfix)

    def get_post_url(self):
        return reverse('add-' + self.url_postfix)

    def _login(self):
        return self.client.login(username=self.user.username, password=self.password)


class TestCategory(BaseCaseMixin, APITestCase):

    def setUp(self):
        self.url_postfix = 'category'
        super(TestCategory, self).setUp()

    def test_add_category(self):
        self._login()
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
        self._login()
        factories.CategoryFactory.create(name='Dogs')
        factories.CategoryFactory.create(name='Cats')
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 2)

    def test_list_category_empty(self):
        self._login()
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Category.objects.count(), 0)

    def test_list_category_unauthenticated(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestNote(BaseCaseMixin, APITestCase):

    def setUp(self):
        self.url_postfix = 'note'
        super(TestNote, self).setUp()

    def test_add_note(self):
        self._login()
        data = {'name': 'Run', 'description': '9 Mile Loop'}
        response = self.client.post(self.post_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Note.objects.count(), 1)
        self.assertEqual(models.Note.objects.get(pk=response.data['id']).name, data['name'])

    def test_list_note_empty(self):
        self._login()
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Note.objects.count(), 0)

    def test_list_note(self):
        factories.NoteFactory.create()
        factories.NoteFactory.create()
        self._login()
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Note.objects.count(), 2)


class TestPlace(BaseCaseMixin, APITestCase):

    def setUp(self):
        self.url_postfix = 'place'
        super(TestPlace, self).setUp()

    def _make_place_data(self):
        note1 = factories.NoteFactory.create()
        note2 = factories.NoteFactory.create()
        cate1 = factories.CategoryFactory.create()
        cate2 = factories.CategoryFactory.create()
        return {'notes': [note1.id, note2.id], 'categories': [cate1.id, cate2.id]}

    def test_add_place(self):
        self._login()
        _place = self._make_place_data()
        data = {
            'name': 'The Zoo',
            'notes': _place['notes'],
            'categories': _place['categories']
        }
        self.assertEqual(models.Place.objects.count(), 0)
        response = self.client.post(self.post_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Place.objects.count(), 1)

    def test_list_place(self):
        factories.PlaceFactory.create()
        self._login()
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.Place.objects.count(), 1)


class TestSpending(BaseCaseMixin, APITestCase):

    def setUp(self):
        self.url_postfix = 'spending'
        super(TestSpending, self).setUp()

    def test_add_spending(self):
        pass

    def test_list_spending(self):
        pass
