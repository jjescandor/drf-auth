from rest_framework import serializers
from .models import EV_Car


class EVCarSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'car_name', 'color', 'range', 'year', 'manufacturer', 'created_at', "updated_at")
        model = EV_Car