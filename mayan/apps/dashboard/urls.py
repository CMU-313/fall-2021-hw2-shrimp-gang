from django.conf.urls import url
from .views import (DashboardView)

urlpatterns_dashboard = [
    url(
        regex=r'^dashboard$', name='document_dashboard_list',
        view=DashboardView.as_view()
    ),
]

urlpatterns = []
urlpatterns.extend(urlpatterns_dashboard)
