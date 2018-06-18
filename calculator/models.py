''' 
Models for the Calculator App
These models determine what fields are pulled
from the cameras and displayed to the user on 
calculator/index.html
'''

from django.db import models
from django.urls import reverse

# try to use this count method for calculating assigned space
# from django.db.models import Count

# INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 73)]

BITRATE_CHOICES = (
    (1024, '1MP'),
    (2048, '2MP'),
    (3072, '3MP'),
    (4096, '4MP'),
    (5120, '5MP'),
    (6144, '6MP'),
    (7168, '7MP'),
    (9192, '8MP'),
)

class Server(models.Model):
    ''' Server class to show server info and add instances Camera class '''
    # <base-root>--><identification>--><server-name>
    server_name = models.CharField(max_length=255)

    # all quota="" attributes from <recordings>
    total_space = models.PositiveIntegerField()

    # number of cameras used in calculating assigned space

    def get_absolute_url(self):
        ''' Used in creating, updating and deleting Server instances '''

        return reverse('calculator:server', kwargs={'pk': self.pk})

    def __str__(self):
        return self.server_name
        

class Camera(models.Model):
    ''' Camera class to display cmaera information after parsed from 
    baseconfig.xml '''
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    # <video-source id="" ...>
    camera_count = models.PositiveIntegerField()

    # <video-source ... descr="" ...>
    camera_model = models.CharField(max_length=255)

    # <stats KBsec=""/> -- will need to convert to Kbps
    avg_bitrate = models.IntegerField(choices = BITRATE_CHOICES)

    # (space on the current path) <autodlt ... max-space="" ...>
    assigned_space = models.PositiveIntegerField()

    # number of days from calculation
    def _get_days(self):
        return str(round(self.camera_count * self.avg_bitrate * 3600 * 24 / self.assigned_space /8/1024/1024, 2))

    rec_days = property(_get_days)

    def __str__(self):
        return self.camera_model
