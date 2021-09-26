from django.template import RequestContext
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

from mayan.apps.views.generics import ( TemplateView )
from .icons import icon_dashboard_link_icon
from .links import (
    link_document_dashboard_list
)


class DashboardView(TemplateView):
    def source_queryset():
        return self.external_object.get_descendants()
    