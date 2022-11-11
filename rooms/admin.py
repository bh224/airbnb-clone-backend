from django.contrib import admin
from .models import Room, Amenity

# Register your models here.
@admin.action(description="Set all prices to Zero")
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()
        

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "rating",
        "total_amenities",
        "owner",
        "created_at",
    )

    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "kind",
        "pet_friendly",
        "toilets",
    )

    search_fields = (
        "^name",
        "=price",
        "owner__username",
    )

    # 어드민패널에서만 사용하는 속성 추가
    # def total_amenities(self, room):
        # print("self", self)
        # print("room", room)
        # return room.amenities.count()


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
    )
