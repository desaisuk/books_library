from django.db import models
from django.utils import timezone


class Issuer(models.Model):
    Id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    Id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField()
    publish_year = models.IntegerField()
    issuer_id = models.ForeignKey(Issuer, on_delete=models.SET(None))
    issue_start_date = models.DateField()
    issue_end_date = models.DateField()

    def __str__(self):
        return self.name


