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
    #owner_list = Owner.objects.all()
    #player_list = Player.objects.filter(kept=True)
    roster_items = Roster.objects.all()

    kevin = Roster.objects.filter(owner__name='Kevin')
    kevin_mcap = Owner.objects.values('cap')[0]['cap']
    temp = Roster.objects.filter(owner__name='Kevin').filter(athlete__kept=True)
    sum = 0
    for item in temp:
        sum = sum + item.athlete.price
    kevin_rcap = kevin_mcap - sum
    template = loader.get_template('liga/rosters.html')
    context = {
     #   'owner_list': owner_list,
     #   'player_list': player_list,
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

