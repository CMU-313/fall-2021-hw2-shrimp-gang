from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import connection, models, transaction
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from mayan.apps.acls.models import AccessControlList
from mayan.apps.databases.model_mixins import ExtraDataModelMixin
from mayan.apps.documents.models.document_models import Document
from mayan.apps.dashboard.permissions import permission_dashboard_view
from mayan.apps.events.classes import EventManagerMethodAfter, EventManagerSave
from mayan.apps.events.decorators import method_event

class Dashboard(models.Model):
    """
    Model to store a hierarchical tree of document containers. Each container
    can store an unlimited number of documents using an M2M field. Only
    the top level container is can have an ACL. All child container's
    access is delegated to their corresponding root container.
    """
    label = models.CharField(
        help_text=_('A short text used to identify the cabinet.'),
        max_length=128, verbose_name=_('Label')
    )
    documents = models.ManyToManyField(
        blank=True, related_name='cabinets', to=Document,
        verbose_name=_('Documents')
    )