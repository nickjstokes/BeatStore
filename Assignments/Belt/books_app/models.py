from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Pasword must be at least 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["do_not_match"] = "Passwords do not match"
        if User.objects.filter(email= postData["email"]):
            errors["already_exists"] = "User already exists"
        return errors

class JobManager(models.Manager):
    def job_validator(self, postData):
        errors = {}
        if len(postData['title']) < 4:
            errors['title'] = "Title must be at least 5 characters"
        if len(postData['description']) < 4:
            errors['description'] = "Description must be at least 5 characters"
        if len(postData['location']) < 4:
            errors['location'] = "Location must be at least 5 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Jobs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    location = models.TextField(null=True)
    uploaded_by = models.ForeignKey(User, related_name="uploaded_by", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
