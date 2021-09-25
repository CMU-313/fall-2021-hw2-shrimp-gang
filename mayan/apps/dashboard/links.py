import copy

from django.utils.translation import ugettext_lazy as _

from mayan.apps.acls.links import link_acl_list
from mayan.apps.documents.permissions import permission_document_view
from mayan.apps.navigation.classes import Link
from mayan.apps.navigation.utils import get_cascade_condition

from .permissions import (
    permission_dashboard_view
)

from .icons import (
    icon_dashboard_link_icon
)

# Document links

link_document_dashboard_list = Link(
    icon=icon_dashboard_link_icon,
    view='dashboard:document_dashboard_list',
    text=_('Dashboard'), permissions = (permission_dashboard_view,)
)


