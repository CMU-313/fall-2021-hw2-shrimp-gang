import copy

from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Link
from .icons import ( icon_dashboard_link_icon )


# Document links

link_document_dashboard_list = Link(
    icon=icon_dashboard_link_icon,
    text=_('Dashboard'), url="/dashboard/dashboard"
)


