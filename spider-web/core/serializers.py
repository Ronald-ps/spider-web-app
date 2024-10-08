from rest_framework import serializers

from core.models import Document, ExternalDocument


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer básico da classe Document (documentos 'internos')"""

    class Meta:
        model = Document
        fields = ["name", "path", "inserted_at", "description"]


class ExternalDocumentSerializer(serializers.ModelSerializer):
    """Serializer básico de ExternalDocument"""

    class Meta:
        model = ExternalDocument
        fields = ["id", "name", "path", "inserted_at", "description"]


class ExternalDocumentSearchSerializer(serializers.Serializer):
    search_text = serializers.CharField()
    max_result_quantity = serializers.IntegerField()
