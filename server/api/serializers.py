from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Study, Task, Test, TimeZone

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ('name', 'stype', 'start', 'end')

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'start', 'end')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fileds = ('name', 'stype', 'studyTime', 'start')

class TimeZoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeZone
        fileds = ('start', 'end')
