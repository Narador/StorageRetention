'''URLS for Calculator App'''

from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'calculator'

urlpatterns = [
    # /calculator/
    path('', views.index, name="index"),

    # /calculator/<server_id>/
    url(r'^(?P<server_id>[0-9]+)/$', views.server, name="server")
]
