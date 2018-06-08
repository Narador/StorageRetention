'''URLS for Calculator App'''

from django.urls import re_path
from . import views

app_name = 'calculator'

urlpatterns = [
    # /calculator/
    re_path('^$', views.IndexView.as_view(), name="index"),

    # /calculator/<server_id>/
    re_path('^(?P<pk>[0-9]+)/$', views.ServerView.as_view(), name="server"),

    # /calculator/<server_id>/
    re_path('^server/add/$', views.ServerCreate.as_view(), name='server-add'),

    # /calculator/<server_id>/
    re_path('^server/(?P<pk>[0-9]+)/edit$', views.ServerUpdate.as_view(), name='server-update'),

    # /calculator/<server_id>/delete/
    re_path('^server/(?P<pk>[0-9]+)/delete/$', views.ServerDelete.as_view(), name='server-delete'),
]
