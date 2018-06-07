'''URLS for Calculator App'''

from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'calculator'

urlpatterns = [
    # /calculator/
    re_path('^$', views.IndexView.as_view(), name="index"),

    # /calculator/<server_id>/
    re_path('^(?P<pk>[0-9]+)/$', views.ServerView.as_view(), name="server"),

    # /calculator/<server_id>/
    re_path('calculator/server/add/$', views.ServerCreate.as_view(), name='server-add')
]
