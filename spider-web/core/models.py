from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db import models

NO_EMPTY = {"null": False, "blank": False}


class ExternalFileSnippet(models.Model):
    """Trecho de um arquivo, indicados por path do arquivo,
    nome, primeira linha e última linha"""

    name = models.TextField(**NO_EMPTY)
    first_line = models.IntegerField(**NO_EMPTY)
    last_line = models.IntegerField(**NO_EMPTY)
    path = models.TextField(**NO_EMPTY)


class Document(models.Model):
    """Documento criado por esse projeto"""

    name = models.TextField(**NO_EMPTY)
    # Nome do document
    path = models.TextField(**NO_EMPTY)
    # Caminho do documento, como um caminho de arquivo no linux
    description = models.TextField(null=True, blank=True)
    # Descrição do documento
    description_search_vector = SearchVectorField(null=True)
    # Descrição traduzida para um search vector, para que seja fácil fazer pesquisa full text
    inserted_at = models.DateTimeField(auto_now_add=True, **NO_EMPTY)
    # Data em que o documento é inserido no banco de dados

    def update_description_search_vector(self):
        """Método utilizado para atualizar o description search vector,
        implementado afim de que não seja necessário atualizar o search vector em runtime"""

        vector = SearchVector("description")
        self.description_search_vector = vector
        self.save(update_fields=["description_search_vector"])

    class Meta:
        indexes = [GinIndex(fields=["description_search_vector"])]


class ExternalDocument(models.Model):
    """Documento externo associado à esse projeto"""

    name = models.TextField(**NO_EMPTY)
    path = models.TextField(**NO_EMPTY)
    inserted_at = models.DateTimeField(auto_now_add=True, **NO_EMPTY)


class ExternalFileSnippetAssociatedDocument(models.Model):
    """Associação entre arquivos externos e documentos"""

    external_file_snippet = models.ForeignKey(to=ExternalFileSnippet, on_delete=models.CASCADE, **NO_EMPTY)
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE, **NO_EMPTY)


class Tag(models.Model):
    """Modelo que representa tags, como 'multa', 'rh' e etc."""

    name = models.TextField(**NO_EMPTY)


class ExternalDocument_Tag(models.Model):
    """Modelo intermediário entre documentos externos (um documento do google docs, por exemplo)
    e tgs (como multa, pagamento, melhoria)"""

    tag = models.ForeignKey(ExternalDocument, on_delete=models.CASCADE, **NO_EMPTY)
    external_document = models.ForeignKey(Tag, on_delete=models.CASCADE, **NO_EMPTY)

    class Meta:
        unique_together = ("tag", "external_document")
