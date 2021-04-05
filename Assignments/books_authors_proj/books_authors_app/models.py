from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True)

class Authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField(null=True)
    books = models.ManyToManyField(Books, related_name="authors")

