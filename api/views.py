# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.machine_learning.models import Task, Test, TimeZone
from api.models import Study
from api.serializers import StudySerializer, TaskSerializer, TestSerializer, TimeZoneSerializer

from machine_learning.processing import processing

@csrf_exempt
def study_list(request):

    if request.method == 'GET':
        studys = Study.objects.all()
        serializer = StudySerializer(studys, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def study_add(request):

    if request.method == 'POST':
        data = JSONPerser().parse(request.data)
        tasks = data.tasks
        tests = data.tests
        """"""
        task_serializer = []
        test_serializer = []
        """"""

        time_zone = TimeZoneSerializer(data=data.time_zone)

        for task in tasks:
            # task_serializer = TaskSerializer(data=task)
            task_serializer.append(TaskSerializer(data=task))
            # task_serializer.save()

        for test in tests:
            # test_serializer = TestSerialzier(data=tests)
            test_serializer.append(TestSerialzier(data=tests))
            # test_serializer.save()

        """
        insert your function here
        """
        # schedule_list = processing(task_list=task_serializer, test_list=test_serializer, time_zones=time_zone)
        #
        # for schedule_days, i in zip(schedule_list, range(len(schedule_list))):
        #     times = pd.period_range(
        #         start=today + datetime.timedelta(days=i + 1),
        #         end=today + datetime.timedelta(days=i + 1) + datetime.timedelta(hours=time_zone.get_hour()),
        #         freq = 'H')
        #     schedule = [i for i in schedule_days if i != 'none']
        #     for sch, time in zip(schedule, times.values[:,0]):
        #         schedule_upload = Study(name=sche.name, stype=sche.stype, start=time, end=time + datetime.timedelta(hours=1))
        #         schedule_upload.save()

        """"""

        return Response(status=status.HTTP_200_OK)
