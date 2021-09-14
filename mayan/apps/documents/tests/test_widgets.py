from __future__ import unicode_literals

from ..widgets import DocumentPageThumbnailWidget

from .test_models import GenericDocumentTestCase


class DocumentPageWidgetTestCase(GenericDocumentTestCase):
    def test_document_list_view_document_with_no_pages(self):
        document_thumbnail_widget = DocumentPageThumbnailWidget()
        self.document.pages.all().delete()
        result = document_thumbnail_widget.render(instance=self.document)

        self.assertTrue(self.document.get_absolute_url() in result)
