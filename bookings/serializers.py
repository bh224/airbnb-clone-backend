from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Booking

class CreateBookingSerializer(ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localtime(timezone.now()).date()
        # 예약일자가 현재보다 과거일 때
        if now > value:
            raise serializers.ValidationError("현재보다 이전 날짜로는 예약할 수 없습니다")
        return value

    def validate_check_out(self, value):
        now = timezone.localtime(timezone.now()).date()
        # 예약일자가 현재보다 과거일 때
        if now > value:
            raise serializers.ValidationError("현재보다 이전 날짜로는 예약할 수 없습니다")
        return value

    def validate(self, data):
        if data['check_out'] <= data['check_in']:
            raise serializers.ValidationError("체크아웃은 체크인 날짜보다 뒤여야 합니다")
        if Booking.objects.filter(
            check_in__lte=data['check_out'],
            check_out__gte=data['check_in'],
        ):
            raise serializers.ValidationError("선택된 날짜에 이미 예약이 있습니다")
        return data

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )