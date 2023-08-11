from django.db import models
from archive.models import ArchiveDocument
from stdimage import StdImageField
from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField, URLField
from stdimage import StdImageField
from archive.consts import *


class Exhibit(models.Model):
    title = models.CharField(max_length=200)
    short_description=models.CharField(max_length=1000)
    items_in_exhibit=models.ManyToManyField(ArchiveDocument)
    exhibit_text = models.TextField(blank=True, null=False)
    def __str__(self):
        return self.title



