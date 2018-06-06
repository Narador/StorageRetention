''' URLS MAIN '''

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include

urlpatterns = [
    re_path('^calculator/', include('calculator.urls')),
    re_path('^admin/', admin.site.urls),
    re_path('^', include('calculator.urls')),
]
