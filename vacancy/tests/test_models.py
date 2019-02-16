from django.test import TestCase
from .factories import VacancyFactory

from vacancy.models import VacancyModel


class VacancyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        VacancyFactory.create()

    def test_str_is_name_(self):
        vacancy = VacancyModel.objects.get(pk=1)
        self.assertEquals(vacancy.name, str(vacancy))


