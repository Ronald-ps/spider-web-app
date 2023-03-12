from rest_framework import permissions, viewsets

from core.models import Document
from core.serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Documents to be viewed or edited.
    """

    queryset = Document.objects.all().order_by("-pk")
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
