from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    file=models.FileField(upload_to='pdfs',default='')
    def __str__(self):
        return self.title