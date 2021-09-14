from __future__ import unicode_literals

from mayan.apps.common.tests import BaseTestCase
from mayan.apps.documents.tests import DocumentTestMixin
from mayan.apps.document_indexing.models import Index, IndexInstanceNode
from mayan.apps.document_indexing.tests.literals import TEST_INDEX_LABEL

from .literals import (
    TEST_TAG_INDEX_HAS_TAG, TEST_TAG_INDEX_NO_TAG, TEST_TAG_INDEX_NODE_TEMPLATE
)
from .mixins import TagTestMixin


class TagSignalIndexingTestCase(TagTestMixin, DocumentTestMixin, BaseTestCase):
    auto_upload_document = False

    def test_tag_indexing(self):
        index = Index.objects.create(label=TEST_INDEX_LABEL)

        index.document_types.add(self.document_type)

        root = index.template_root
        index.node_templates.create(
            parent=root, expression=TEST_TAG_INDEX_NODE_TEMPLATE,
            link_documents=True
        )

        self._create_test_tag()

        self.document = self.upload_document()

        self.assertTrue(
            self.document in IndexInstanceNode.objects.get(
                value=TEST_TAG_INDEX_NO_TAG
            ).documents.all()
        )

        self.test_tag.documents.add(self.document)

        self.assertTrue(
            self.document in IndexInstanceNode.objects.get(
                value=TEST_TAG_INDEX_HAS_TAG
            ).documents.all()
        )

        self.test_tag.delete()

        self.assertTrue(
            self.document in IndexInstanceNode.objects.get(
                value=TEST_TAG_INDEX_NO_TAG
            ).documents.all()
        )
