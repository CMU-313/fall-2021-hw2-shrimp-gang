from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db import connection, models, transaction
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from mayan.apps.acls.models import AccessControlList
from mayan.apps.databases.model_mixins import ExtraDataModelMixin
from mayan.apps.documents.models.document_models import Document
from mayan.apps.dashboard.permissions import permission_dashboard_view
from mayan.apps.events.classes import EventManagerMethodAfter, EventManagerSave
from mayan.apps.events.decorators import method_event

class Dashboard(ExtraDataModelMixin, MPTTModel):
    """
    Model to store a hierarchical tree of document containers. Each container
    can store an unlimited number of documents using an M2M field. Only
    the top level container is can have an ACL. All child container's
    access is delegated to their corresponding root container.
    """
    parent = TreeForeignKey(
        blank=True, db_index=True, null=True, on_delete=models.CASCADE,
        related_name='children', to='self'
    )
    label = models.CharField(
        help_text=_('A short text used to identify the cabinet.'),
        max_length=128, verbose_name=_('Label')
    )
    documents = models.ManyToManyField(
        blank=True, related_name='cabinets', to=Document,
        verbose_name=_('Documents')
    )

    class MPTTMeta:
        order_insertion_by = ('label',)

    class Meta:
        # unique_together doesn't work if there is a FK
        # https://code.djangoproject.com/ticket/1751
        unique_together = ('parent', 'label')
        verbose_name = _('Cabinet')
        verbose_name_plural = _('Cabinets')

    def __str__(self):
        return self.get_full_path()