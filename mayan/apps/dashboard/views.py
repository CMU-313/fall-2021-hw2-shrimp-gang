# from django.template import RequestContext
# from django.urls import reverse_lazy
# from django.utils.translation import ugettext_lazy as _

# from mayan.apps.views.generics import ( SingleObjectListView )
# from .icons import icon_dashboard_link_icon
# from .links import (
#     link_document_dashboard_list
# )

# # class DashboardView(SingleObjectListView):

# #     def get_extra_context(self):
# #         return {
# #             'hide_link': True,
# #             'hide_object': True,
# #             'title': _('Dashboard'),
# #             'no_results_icon': icon_dashboard_link_icon,
# #             'no_results_main_link': link_document_dashboard_list.resolve(
# #                 context=RequestContext(request=self.request)
# #             ),
# #             'no_results_text': _('...'),
# #             'no_results_title': _('No dashboard available'),
# #         } 

# class DashboardView(TemplateView):
#     def source_queryset():
#         return self.external_object.get_descendants()

from django.http import HttpResponse
from django.views import View

class DashboardView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')