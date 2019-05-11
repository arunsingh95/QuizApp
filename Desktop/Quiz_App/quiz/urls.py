# from django.ur#ls import  urls#,urlpatterns
from django.conf.urls import url, include

from .views import *

app_name = 'quiz'

urlpatterns = [
							url(r'^$', first_view, name='first_view'),
							url(r'questions_list/(?P<id>[0-9]+)/$', questions_list, name='questions_list'),
							url(r'results', Result, name='results'),
							url(r'timer', timer, name='timer'),
							# url(r'<int:question_id>/detail', detail, name='detail'),
							]