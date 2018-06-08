''' 
Models for the Calculator App
These models determine what fields are pulled
from the cameras and displayed to the user on 
calculator/index.html
'''

from django.db import models
from django.urls import reverse

class Server(models.Model):
    ''' Server class to show server info and add instances Camera class '''
    # <base-root>--><identification>--><server-name>
    server_name = models.CharField(max_length=255)

    # NO WAY TO PARSE FROM XML...
    # serial_number = models.CharField(max_length=9)

    # NO WAY TO PARSE FROM XML...
    # server_version = models.CharField(max_length=50)

    # all quota="" attributes from <recordings>
    total_space = models.CharField(max_length=20)

    # iterate through Camera class objects
    camera_count = models.CharField(max_length=3)

    # check to see if application running
    server_status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('calculator:server', kwargs={'pk': self.pk})

    def __str__(self):
        return self.server_name

class Camera(models.Model):
    ''' Camera class to display cmaera information after parsed from 
    baseconfig.xml '''
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    # <video-source id="" ...>
    camera_number = models.CharField(max_length=3)

    # <video-source ... descr="" ...>
    camera_name = models.CharField(max_length=255)

    # <s-params ... addr="192.168.1.114" ...>
    camera_address = models.CharField(max_length=15)

    # <stats KBsec=""/> -- will need to convert to Kbps
    avg_bitrate = models.CharField(max_length=20)

    # <dvrcfg ena="" ...>
    rec_enabled = models.BooleanField(default=False)

    # <autodlt ... max-space-type="auto" ...>
    delete_type = models.CharField(max_length=4)

    # (space on the current path) <autodlt ... max-space="" ...>
    assigned_space = models.CharField(max_length=15)

    # number of days from calculation
    rec_days = models.CharField(max_length=5)

    def __str__(self):
        return self.camera_name