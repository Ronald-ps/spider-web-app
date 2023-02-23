from rest_framework import serializers

from core.models import Document


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ["name", "path"]
