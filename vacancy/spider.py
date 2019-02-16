from grab.spider import Spider, Task
from .models import VacancyModel
import re

import warnings
warnings.filterwarnings("ignore")


class VacancySpider(Spider):
    initial_urls = ['https://spb.hh.ru/employer/889']

    @classmethod
    def get_salary_data(cls, salary_string):
        salary_data = {}

        salary_from_string = re.search("от (\d{1,3} ){1,3}", salary_string)
        salary_to_string = re.search("до (\d{1,3} ){1,3}", salary_string)
        currency = re.search("(USD|EUR|руб.)", salary_string)

        if salary_from_string:
            salary_from = salary_from_string.group(0)[3:-1].replace(' ', '')
            salary_data.update({'salary_from': int(salary_from)})

        if salary_to_string:
            salary_to = salary_to_string.group(0)[3:-1].replace(' ', '')
            salary_data.update({'salary_to': int(salary_to)})

        if currency:
            salary_data.update({'currency': currency.group(0)})

        return salary_data

    def task_initial(self, grab, task):
        for elem in grab.xpath_list(".//div[@class='resume-search-item__name']/a"):
            yield Task('update_vacancy_data', url=elem.get('href'))

    def task_update_vacancy_data(self, grab, task):
        link = task.url
        name = grab.xpath_text(".//h1")
        short_description = grab.xpath_text(".//div[@class='g-user-content']")[0:250]
        description = grab.xpath_text(".//div[@class='g-user-content']")

        salary_string = grab.xpath_text(".//p[@class='vacancy-salary']")

        salary_data = self.get_salary_data(salary_string)

        VacancyModel.objects.create(
            name=name, short_description=short_description,
            description=description, link=link, **salary_data
        ).save()




