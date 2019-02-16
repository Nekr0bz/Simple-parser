from django.test import TestCase
from .factories import VacancyFactory


class VacancyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.vacancy = VacancyFactory.create()

    def test_str_is_name_(self):
        self.assertEquals(self.vacancy.name, str(self.vacancy))

    def test_get_absolute_url(self):
        vacancy_id = self.vacancy.id
        self.assertEquals(self.vacancy.get_absolute_url(), '/vacancy/{}/'.format(vacancy_id))


