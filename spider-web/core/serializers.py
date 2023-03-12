from rest_framework import serializers

from core.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer básico da classe Document (documentos 'internos')"""

    class Meta:
        model = Document
        fields = ["name", "path", "inserted_at"]
