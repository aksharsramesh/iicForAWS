from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class newIdea(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    UPI_transaction_ID = models.CharField(max_length = 100)
    document = models.FileField(upload_to='documents/', blank=True)
    date = models.DateTimeField(auto_now_add = True)
    contact = models.CharField(max_length = 13)

    def __str__(self):
        return self.title
