from rest_framework import serializers

from .models import User, Record


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class TimelineSerializer(serializers.BaseSerializer):

    def records_to_timeline(self, records):
        pass
