from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import VacancyModel


class IndexPageView(TemplateView):
    template_name = "index.html"


class VacancyListView(ListView):
    template_name = "list.html"
    model = VacancyModel


class VacancyDetailView(DetailView):
    template_name = "detail.html"
    model = VacancyModel

