from django.http import HttpResponse

from .models import Owner
from .models import Player
from .models import Roster
from django.template import loader


def index(request):
    #owner_list = Owner.objects.all()
    template = loader.get_template('liga/index.html')
    context = {
        #'owner_list': owner_list,
    }
    return HttpResponse(template.render(context, request))


def rosters(request):
    roster_items = Roster.objects.all()

    kevin = Roster.objects.filter(owner__name='Kevin')
    kevin_mcap = Owner.objects.values('cap')[0]['cap']
    kevin_rcap = remaining('Kevin', kevin_mcap)

    template = loader.get_template('liga/rosters.html')
    context = {
        'roster_items': roster_items,
        'kevin': kevin,
        'kevin_mcap': kevin_mcap,
        'kevin_rcap': kevin_rcap,
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


def remaining(name, max):
    temp = Roster.objects.filter(owner__name=name).filter(athlete__kept=True)
    sum = 0
    for item in temp:
        sum = sum + item.athlete.price
    return max - sum

