from django.conf.urls import url

from mayan.apps.views.generics import (
    SingleObjectCreateView, SingleObjectDeleteView, SingleObjectEditView,
    SingleObjectListView, SimpleView
)

urlpatterns_dashboard = [
    url(
        regex=r'^dashboard/from mayan.apps.views.generics import (
    SingleObjectCreateView, SingleObjectDeleteView, SingleObjectEditView,
    SingleObjectListView, SimpleView
)$', name='dashboard_list',
        view=SimpleView.as_view()
    ),
]

urlpatterns = []
urlpatterns.extend(urlpatterns_dashboard)

# api_urls = [
#     url(
#         regex=r'^cabinets/(?P<cabinet_id>[0-9]+)/$', name='cabinet-detail',
#         view=APICabinetView.as_view()
#     ),
#     url(
#         regex=r'^cabinets/$', name='cabinet-list',
#         view=APICabinetListView.as_view()
#     ),
#     url(
#         regex=r'^cabinets/(?P<cabinet_id>[0-9]+)/documents/$',
#         name='cabinet-document-list',
#         view=APICabinetDocumentListView.as_view()
#     ),
#     url(
#         regex=r'^cabinets/(?P<cabinet_id>[0-9]+)/documents/add/$',
#         name='cabinet-document-add', view=APICabinetDocumentAddView.as_view()
#     ),
#     url(
#         regex=r'^cabinets/(?P<cabinet_id>[0-9]+)/documents/remove/$',
#         name='cabinet-document-remove', view=APICabinetDocumentRemoveView.as_view()
#     ),
#     url(
#         regex=r'^documents/(?P<document_id>[0-9]+)/cabinets/$',
#         name='document-cabinet-list',
#         view=APIDocumentCabinetListView.as_view()
#     ),
# ]
