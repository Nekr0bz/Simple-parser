from django.urls import path
from .views import IndexPageView, VacancyListView, VacancyDetailView, GenerateDataView

app_name = 'vacancy'
urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('vacancy/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancy/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('generate/', GenerateDataView.as_view(), name='generate'),
]
