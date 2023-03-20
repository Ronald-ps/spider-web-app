from django.contrib.postgres.search import SearchQuery, SearchRank
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from core.models import ExternalDocument
from core.serializers import (
    ExternalDocumentSearchSerializer,
    ExternalDocumentSerializer,
)


def hello(request):
    return JsonResponse({"ola": "mundo"})


@api_view(["GET"])
def search_documents(request):
    serializer = ExternalDocumentSearchSerializer(data=request.GET)
    if not serializer.is_valid():
        raise ParseError(detail=serializer.errors, code="invalid")
    search_text = serializer.data["search_text"]
    max_result_quantity = serializer.data["max_result_quantity"]
    documents = ExternalDocument.objects.annotate(
        rank=SearchRank("description_search_vector", SearchQuery(search_text, config="portuguese"))
    ).order_by("-rank", "-id")[:max_result_quantity]

    response_data = ExternalDocumentSerializer(documents, many=True).data
    return Response(response_data)
