from django.apps import apps
from django.utils.translation import ugettext_lazy as _

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.acls.permissions import permission_acl_edit, permission_acl_view
from mayan.apps.common.apps import MayanAppConfig
from mayan.apps.common.classes import ModelCopy, ModelQueryFields
from mayan.apps.common.menus import (
    menu_facet, menu_list_facet, menu_main, menu_multi_item, menu_object,
    menu_secondary
)

from .links import (
    link_document_dashboard_list
)

class DashboardApp(MayanAppConfig):
    app_namespace = 'dashboard'
    app_url = 'dashboard'
    has_rest_api = False
    has_tests = False
    name = 'mayan.apps.dashboard'
    verbose_name = _('Dashboard')
    def ready(self):
        super().ready()
        menu_main.bind_links(links=(link_document_dashboard_list,), position=99) 
    