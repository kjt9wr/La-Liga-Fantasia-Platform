from django.http import HttpResponse

from .models import Owner
from .models import Player
from django.template import loader


def index(request):
    #owner_list = Owner.objects.all()
    template = loader.get_template('liga/index.html')
    context = {
        #'owner_list': owner_list,
    }
    return HttpResponse(template.render(context, request))


def rosters(request):
    owner_list = Owner.objects.all()
    template = loader.get_template('liga/rosters.html')
    context = {
        'owner_list': owner_list,
    }
    return HttpResponse(template.render(context, request))


def captracker(request):
    owner_list = Owner.objects.all()
    template = loader.get_template('liga/captracker.html')
    context = {
        'owner_list': owner_list,
    }
    return HttpResponse(template.render(context, request))


def franchise(request):
    player_list = Player.objects.filter(kept=True)
    template = loader.get_template('liga/franchise.html')
    context = {
        'player_list': player_list,
    }
    return HttpResponse(template.render(context, request))

