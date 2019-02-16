from django.test import TestCase
from django.urls import reverse
import random

from vacancy.models import VacancyModel
from .factories import VacancyFactory


class IndexViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('vacancy:index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('vacancy:index'))
        self.assertTemplateUsed(resp, 'index.html')


class ListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        VacancyFactory.create_batch(5)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/vacancy/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('vacancy:vacancy_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('vacancy:vacancy_list'))
        self.assertTemplateUsed(resp, 'list.html')

    def test_view_have_correct_len_list_objects(self):
        resp = self.client.get(reverse('vacancy:vacancy_list'))
        object_list = resp.context['object_list']
        self.assertTrue(len(object_list) == 5)

    def test_view_have_correct_type_list_objects(self):
        resp = self.client.get(reverse('vacancy:vacancy_list'))
        object_list = resp.context['object_list']
        for obj in object_list:
            self.assertTrue(isinstance(obj, VacancyModel))


class DetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.vacancy_id = VacancyFactory.create().id

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/vacancy/{}/'.format(self.vacancy_id))
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('vacancy:vacancy_detail', args=[self.vacancy_id]))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('vacancy:vacancy_detail', args=[self.vacancy_id]))
        self.assertTemplateUsed(resp, 'detail.html')

    def test_HTTP404_for_invalid_args(self):
        numbers = list(range(5))

        if self.vacancy_id in numbers:
            numbers.remove(self.vacancy_id)

        invalid_id = random.choice(numbers)
        resp = self.client.get(reverse('vacancy:vacancy_detail', args=[invalid_id]))
        self.assertEqual(resp.status_code, 404)

    def test_view_have_correct_type_context_object(self):
        resp = self.client.get(reverse('vacancy:vacancy_detail', args=[self.vacancy_id]))
        obj = resp.context['object']
        self.assertTrue(isinstance(obj, VacancyModel))

