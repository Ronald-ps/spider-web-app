from rest_framework import serializers

from core.models import Document, ExternalDocument


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer básico da classe Document (documentos 'internos')"""

    class Meta:
        model = Document
        fields = ["name", "path", "inserted_at"]


class ExternalDocumentSerializer(serializers.ModelSerializer):
    """Serializer básico de ExternalDocument"""

    class Meta:
        model = ExternalDocument
        fields = "__all__"
