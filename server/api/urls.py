from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
            url(r'^api/create/$', views.study_add),
            url(r'^api/show/$', views.study_list),
            ]

urlpatterns = format_suffix_patterns(urlpatterns)
