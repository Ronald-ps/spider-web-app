from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.decorators import action

from core.models import Document, ExternalDocument
from core.serializers import DocumentSerializer, ExternalDocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite a CRUD de Document
    """

    queryset = Document.objects.all().order_by("-pk")
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "path"]


class ExternalDocumentViewSet(viewsets.ModelViewSet):
    """
    Endpoint que permite a CRUD de ExternalDocument
    """

    queryset = ExternalDocument.objects.all().order_by("-pk")
    serializer_class = ExternalDocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Modificada para que eu salve o vetor de pesquisa full text, talvez colocar o id em cache
        # e atualizar esse cara depois seja uma opção melhor
        document = ExternalDocument.objects.create(**serializer.validated_data)
        document.update_description_search_vector()
        return document

    def perform_update(self, serializer):
        # Modificada para que eu salve o vetor de pesquisa full text, talvez colocar o id em cache
        # e atualizar esse cara depois seja uma opção melhor
        id = ExternalDocument.objects.filter(id=serializer.data["id"]).update(**serializer.validated_data)
        ExternalDocument.objects.get(id=id).update_description_search_vector()
        # Sim, está pesado, mas estava com preguiça de aprender mais sobre cache agora
