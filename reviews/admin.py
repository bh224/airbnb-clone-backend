from django.contrib import admin
from .models import Review
from django.db.models import Q

# Register your models here.
class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return reviews


# 평점 3이상 좋은 리뷰 필터
class GoodReviewFilter(admin.SimpleListFilter):
    title = "Good or Bad Review"
    parameter_name = "goodorbad"

    keyword_filter = {
        "good": "gte",
        "bad": "lt",
    }

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        keyword = self.value()
        if keyword:
            filter_set = {f"rating__{self.keyword_filter[keyword]}": 3}
            # print(filter_set)
            return reviews.filter(Q(payload__contains="great"), **filter_set)
        return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        GoodReviewFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
