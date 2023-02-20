from django.db import models


class ExternalFileSnippet(models.Model):
    """Trecho de um arquivo, indicados por path do arquivo,
    nome, primeira linha e última linha"""

    name = models.TextField(null=False, blank=False)
    first_line = models.IntegerField(null=False, blank=False)
    last_line = models.IntegerField(null=False, blank=False)
    path = models.TextField(null=False, blank=False)


class Document(models.Model):
    """ Documento criado por esse projeto """
    pass
