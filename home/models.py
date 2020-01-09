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
    f2 = models.BigIntegerField(null=True, blank=True,)

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
    f4 = models.OneToOneField(
        "home.HomePage",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="r1_f4",
    )


class R5(models.Model):
    "Generated Model"
    f1 = models.BigIntegerField()
    f2 = models.BigIntegerField()
    f3 = models.CharField(max_length=256,)
    f4 = models.BigIntegerField(null=True, blank=True,)
    f5 = models.ForeignKey(
        "home.CustomText",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="r5_f5",
    )


class R6(models.Model):
    "Generated Model"
    f1 = models.DateField()
    f2 = models.TimeField(auto_now=True,)
    f3 = models.DateTimeField(auto_now_add=True,)
    f4 = models.ForeignKey(
        "home.R1",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="r6_f4",
    )
    f5 = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="r6_f5",
    )


class R56(models.Model):
    "Generated Model"
    f1 = models.ForeignKey("home.R1", on_delete=models.CASCADE, related_name="r56_f1",)


class R57(models.Model):
    "Generated Model"
    f1 = models.ForeignKey(
        "home.CustomText", on_delete=models.CASCADE, related_name="r57_f1",
    )
