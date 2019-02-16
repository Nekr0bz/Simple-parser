from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from celery.result import AsyncResult
from django.http import JsonResponse
from django.http import Http404

from .models import VacancyModel
from .tasks import generate_vacancy_data


class IndexPageView(TemplateView):
    template_name = "index.html"


class VacancyListView(ListView):
    template_name = "list.html"
    model = VacancyModel


class VacancyDetailView(DetailView):
    template_name = "detail.html"
    model = VacancyModel


class GenerateDataView(TemplateView):
    template_name = "preloader.html"

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            task = AsyncResult(self.request.session.get('task_uuid'))
            return JsonResponse({'task_status': task.state})
        else:
            raise Http404

    def post(self, request, *args, **kwargs):
        task = generate_vacancy_data.delay()
        self.request.session['task_uuid'] = task.id
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

