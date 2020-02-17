from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class newIdea(models.Model):
    Title_Of_Idea = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    UPI_transaction_ID = models.CharField(max_length = 100)
    Your_UPI_ID = models.CharField(max_length = 100, blank = True)
    document = models.FileField(upload_to='documents/', blank=True)
    date = models.DateTimeField(auto_now_add = True)
    Contact_Number = models.CharField(max_length = 13)

    def __str__(self):
        return self.title
