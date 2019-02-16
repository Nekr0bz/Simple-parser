from django.db import models
from django.urls import reverse


class VacancyModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Назвние вакансии")
    short_description = models.TextField(verbose_name="Краткое описание вакансии")
    description = models.TextField(verbose_name="Описание вакансии")
    salary_from = models.IntegerField(verbose_name="з/п от", blank=True, null=True)
    salary_to = models.IntegerField(verbose_name="з/п до", blank=True, null=True)
    currency = models.CharField(max_length=4, verbose_name="Валюта з/п", blank=True, null=True)
    link = models.URLField(max_length=60, verbose_name="Ссылка на вакансию")

    class Meta:
        db_table = 'Vacancy'
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def get_absolute_url(self):
        return reverse('vacancy:vacancy_detail', args=[self.id])

    def __str__(self):
        return self.name

