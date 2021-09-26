from django.conf.urls import url
from .views import (DashboardView)

urlpatterns_dashboard = [
    url(
        regex=r'^dashboard$', name='document_dashboard_list',
        view=DashboardView.as_view()
    ),
]
# Adds new URL link to the list of URLs so that dashboard tab properly directs to the correct site on the page.
urlpatterns = []
urlpatterns.extend(urlpatterns_dashboard)
