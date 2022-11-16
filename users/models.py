from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    # 기존 장고유저모델에 있는 필드를 오버로드해서 사용하지 않도록 함
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("femail", "Femail")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean  Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    avatar = models.URLField(blank=True)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)
