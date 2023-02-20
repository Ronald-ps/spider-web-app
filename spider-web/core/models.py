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

    pass


class ExternalFileSnippetAssociatedDocument(models.Model):
    """Associação entre arquivos externos e documentos"""

    external_file_snippet = models.ForeignKey(to=ExternalFileSnippet, on_delete=models.CASCADE, **NO_EMPTY)
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE, **NO_EMPTY)
