from django.utils.translation import ugettext_lazy as _

from mayan.apps.common.apps import MayanAppConfig


class DashboardApp(MayanAppConfig):
    app_namespace = 'dashboard'
    app_url = 'dashboard'
    has_rest_api = False
    has_tests = False
    name = 'mayan.apps.dashboard'
    verbose_name = _('Dashboard')
