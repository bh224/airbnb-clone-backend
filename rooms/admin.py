from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "kind",
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
