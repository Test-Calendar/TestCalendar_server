from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.models import Study

class StudySerializer(serializer.HyperLinkedModelSerializer):
    class Meta:
        model = Study
        fields = ('name', 'stype', 'start', 'end')
