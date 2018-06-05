''' VIEWS CALCULATOR '''

from django.shortcuts import render, get_object_or_404
from .models import Server

def index(request):
    ''' Points to the index of the calculator app '''
    all_servers = Server.objects.all()
    return render(request, 'calculator/index.html', {'all_servers': all_servers})


def server(request, server_id):
    # server = Server.objects.get(id=server_id)
    server = get_object_or_404(Server, id=server_id)
    return render(request, 'calculator/server.html', {'server': server})

