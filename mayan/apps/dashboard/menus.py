from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Menu
from mayan.apps.navigation.utils import get_cascade_condition

from .icons import icon_cabinet_list
from .permissions import permission_dashboard_view

menu_dashboard = Menu(
     condition=get_cascade_condition(
        app_label='Dashboard', model_name='Dashboard',
        object_permission=permission_dashboard_view,
        view_permission=permission_dashboard_view,
    ), icon=icon_cabinet_list, label=_('Dashboard'), name='Dashboard'
)
