from django.db import models

# Create your models here.

class TestModel(models.Model):
    test_title = models.CharField(max_length=255)
