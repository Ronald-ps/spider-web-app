from rest_framework import permissions, viewsets

from core.models import Document, ExternalDocument
from core.serializers import DocumentSerializer, ExternalDocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite a CRUD de Document
    """

    queryset = Document.objects.all().order_by("-pk")
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExternalDocumentViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite a CRUD de ExternalDocument
    """

    queryset = ExternalDocument.objects.all().order_by("-pk")
    serializer_class = ExternalDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
