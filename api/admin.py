# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Study, TimeZone, Task, Test

# Register your models here.
admin.site.register(Study)
admin.site.register(TimeZone)
admin.site.register(Task)
admin.site.register(Test)
