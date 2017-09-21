# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONPerser
from api.models import Study, Task, Test, TimeZone
from api.serializer import StudySerializer

def study_list(request):

    if request.method == 'GET':
        studys = Study.objects.all()
        serializer = StudySerializer(studys, many=True)
        return JsonResponse(serializer.data, safe=False)


