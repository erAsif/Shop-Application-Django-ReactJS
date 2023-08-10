from rest_framework import serializers
from .models import Profile,TimeSchedule,Performance

class TimeScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSchedule
        fields = '__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    staffschedule = TimeScheduleSerializer(many=True, read_only=True)
    staffperformance = PerformanceSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
