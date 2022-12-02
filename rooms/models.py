from django.db import models
from common.models import CommonModel

# Create your models here.
class Room(CommonModel):
    """RoomModel"""
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_PLACE = ("private_place", "Private Place")
        SHARED_PLACE = ("shared_place", "Shared Place")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="한국")
    city = models.CharField(max_length=80, default="서울")
    price =models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms")
    amenities = models.ManyToManyField("rooms.Amenity", related_name="rooms")
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, blank=True, null=True, related_name="rooms")

    def __str__(self):
        return self.name

    #  어드민패널의 속성 추가
    def total_amenities(self):
        return self.amenities.count()

    # 방 리뷰 평점 평균
    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return 0
        else:
            total_rating = 0
            for review in self.reviews.all().values("rating"):
                total_rating += review["rating"]
            return round(total_rating / count, 2)

class Amenity(CommonModel):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True, blank=True)

    #해당 데이터 객체의 이름 변경
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"