''' VIEWS CALCULATOR 

from django.shortcuts import render, get_object_or_404
from .models import Server

def index(request):
    Points to the index of the calculator app 
    all_servers = Server.objects.all()
    return render(request, 'calculator/index.html', {'all_servers': all_servers})


def server(request, server_id):
    server = Server.objects.get(id=server_id) 
    server = get_object_or_404(Server, id=server_id)
    return render(request, 'calculator/server.html', {'server': server})
'''

# GENERIC VIEWS ---------------------------------------

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Server

class IndexView(generic.ListView):
    ''' Index view for showing Servers list '''
    template_name = "calculator/index.html"
    context_object_name = "all_servers"

    def get_queryset(self):
        return Server.objects.all()

class ServerView(generic.DetailView):
    ''' Detail view showing cameras on a Server '''
    model = Server
    template_name = "calculator/server.html"


class ServerCreate(CreateView):
    ''' Create Server View '''
    model = Server
    fields = ['server_name', 'total_space']

class ServerUpdate(UpdateView):
    ''' Update Server View '''
    model = Server
    fields = ['server_name', 'total_space']

class ServerDelete(DeleteView):
    ''' Delete Server View (goes back to index after delete) '''
    model = Server
    success_url = reverse_lazy('calculator:index')

#------------------------------------------------------
