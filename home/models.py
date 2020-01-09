from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class R1(models.Model):
    "Generated Model"
    f1 = models.DateField()
    f2 = models.DateTimeField(auto_now=True,)
    f3 = models.TimeField(auto_now_add=True,)


class R5(models.Model):
    "Generated Model"
    f1 = models.BigIntegerField()
    f2 = models.BigIntegerField()
    f3 = models.CharField(max_length=256,)
    f4 = models.BigIntegerField(null=True, blank=True,)
