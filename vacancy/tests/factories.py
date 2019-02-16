import factory.fuzzy

from vacancy.models import VacancyModel


class VacancyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = VacancyModel

    name = factory.fuzzy.FuzzyText()
