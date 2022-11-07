from django.db import models
from common.models import CommonModel

# Create your models here.

class Experience(CommonModel):
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="experiences")
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description= models.TextField()
    perks = models.ManyToManyField("experiences.Perk", related_name="experiences")
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, blank=True, null=True, related_name="experiences")

    def __str__(self):
        return self.name

class Perk(CommonModel):
    name = models.CharField(max_length=150)
    details = models.CharField(max_length=250, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
