from django.utils.translation import ugettext_lazy as _

from mayan.apps.permissions import PermissionNamespace

namespace = PermissionNamespace(label=_('Dashboard'), name='Dashboard')

permission_dashboard_view = namespace.add_permission(
    label=_('View'), name='dashboard_view'
)

