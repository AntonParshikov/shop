from django.urls import path
from django.views.decorators.cache import cache_page

from statistic.apps import StatisticConfig
from statistic.views import StatisticCreateView, StatisticListView, StatisticDetailView, StatisticUpdateView, \
    StatisticDeleteView

app_name = StatisticConfig.name

urlpatterns = [
    path('create/', StatisticCreateView.as_view(), name='create'),
    path('statistic/', cache_page(60)(StatisticListView.as_view()), name='list'),
    path('view/<int:pk>/', StatisticDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', StatisticUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', StatisticDeleteView.as_view(), name='delete'),
]
