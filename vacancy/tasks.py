from simpleParser.celery import app

from .models import VacancyModel
from .spider import VacancySpider

@app.task
def generate_vacancy_data():
    VacancyModel.objects.all().delete()
    bot = VacancySpider(thread_number=10)
    bot.run()

