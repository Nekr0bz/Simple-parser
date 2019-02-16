from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView


class IndexPageView(TemplateView):
    template_name = "index.html"


class VacancyListView(ListView):
    pass


class VacancyDetailView(DetailView):
    pass

