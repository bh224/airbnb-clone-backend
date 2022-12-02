from rest_framework import serializers
from .models import Category

class CatgegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # exclude = ("created_at")
        fields = ("pk", "name", "kind",)