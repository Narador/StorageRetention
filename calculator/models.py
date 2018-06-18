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

INTEGER_CHOICES = [tuple([x, x]) for x in range(1, 73)]

BITRATE_CHOICES = (
    ('1MP', '1024'),
    ('2MP', '2048'),
    ('3MP', '3072'),
    ('4MP', '4096'),
    ('5MP', '5120'),
    ('6MP', '6144'),
    ('7MP', '7168'),
    ('8MP', '9192'),
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
    camera_number = models.CharField(max_length=3)

    # <video-source ... descr="" ...>
    camera_name = models.CharField(max_length=255)

    # <stats KBsec=""/> -- will need to convert to Kbps
    avg_bitrate = models.CharField(max_length=4, choices = BITRATE_CHOICES)

    # (space on the current path) <autodlt ... max-space="" ...>
    assigned_space = models.CharField(max_length=20)

    # number of days from calculation
    rec_days = models.CharField(max_length=5)

    def __str__(self):
        return self.camera_name
