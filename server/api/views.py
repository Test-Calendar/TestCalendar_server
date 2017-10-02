# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Study, Task, Test, TimeZone
from api.serializers import StudySerializer, TaskSerializer, TestSerializer

# from machine_learning.processing import processing

@csrf_exempt
def study_list(request):

    if request.method == 'GET':
        studys = Study.objects.all()
        serializer = StudySerializer(studys, many=True)
        return JsonResponse(serializer.data, safe=False)

# @csrf_exempt
# def test_list(request):
#
#     if request.method == 'GET':
#         tests = Test.objects.all()
#         serializer = StudySerializer(tests, many=True)
#         return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def study_add(request):

    if request.method == 'POST':
        data = JSONPerser().parse(request.data)
        tasks = data.tasks
        tests = data.tests
        for task in tasks:
            task_serializer = TaskSerializer(data=task)
            task_serializer.save()

        for test in tests:
            test_serializer = TestSerialzier(data=tests)
            test_serializer.save()

        """
        insert your function here
        """

        return Response(status=status.HTTP_200_OK)
