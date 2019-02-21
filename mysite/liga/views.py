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


def rosters(request, owner_id):
    roster_items = Roster.objects.all()

    kevin = Roster.objects.filter(owner__pk=owner_id)
    owner_name = Owner.objects.filter(pk=owner_id).values('name')[0]['name']
    max_cap = Owner.objects.filter(pk=owner_id).values('cap')[0]['cap']
    rem_cap = remaining(owner_name, max_cap)

    template = loader.get_template('liga/rosters.html')
    context = {
        'roster_items': roster_items,
        'kevin': kevin,
        'max_cap': max_cap,
        'owner_name': owner_name,
        'rem_cap': rem_cap,
    }
    return HttpResponse(template.render(context, request))


def remaining(name, max):
    temp = Roster.objects.filter(owner__name=name).filter(athlete__kept=True)
    sum = 0
    for item in temp:
        sum = sum + item.athlete.price
    return max - sum

