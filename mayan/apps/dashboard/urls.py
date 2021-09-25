from django.conf.urls import url

from mayan.apps.views.generics import (
    SingleObjectCreateView, SingleObjectDeleteView, SingleObjectEditView,
    SingleObjectListView, SimpleView
)

urlpatterns_dashboard = [
    url(
        regex=r'^dashboard$', name='dashboard_view',
        view=SimpleView.as_view()
    ),
]

urlpatterns = []
urlpatterns.extend(urlpatterns_dashboard)