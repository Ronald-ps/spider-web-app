from django.db import models


class ExternalFileSnippet(models.Model):
    """Trecho de um arquivo, indicados por path do arquivo,
    nome, primeira linha e última linha"""

    name = models.TextField(null=False, blank=False)
    first_line = models.IntegerField(null=False, blank=False)
    last_line = models.IntegerField(null=False, blank=False)
    path = models.TextField(null=False, blank=False)


class Document(models.Model):
    """Documento criado por esse projeto"""

    pass


class ExternalFileSnippetAssociatedDocument(models.Model):
    """Associação entre arquivos externos e documentos"""

    external_file_snippet = models.ForeignKey(to=ExternalFileSnippet, on_delete=models.CASCADE, null=False, blank=False)
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE, null=False, blank=False)
