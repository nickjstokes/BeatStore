from django.db import models

class FormManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title must be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network must be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Description must be at least 10 characters"
        return errors

class All_Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField(max_length=45, null=True)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = FormManager()