from django.http import HttpResponse
from django.shortcuts import render

from .models import Owner
from .models import Player
from .models import Roster
from django.template import loader


def index(request):
    context = {}
    return render(request, 'liga/index.html', context)



def rosters(request, owner_id):
    roster_items = Roster.objects.all()

    kevin = Roster.objects.filter(owner__pk=owner_id)
    owner_name = Owner.objects.filter(pk=owner_id).values('name')[0]['name']
    max_cap = Owner.objects.filter(pk=owner_id).values('cap')[0]['cap']
    rem_cap = remaining(owner_name, max_cap)
    context = {
        'roster_items': roster_items,
        'kevin': kevin,
        'max_cap': max_cap,
        'owner_name': owner_name,
        'rem_cap': rem_cap,
    }
    return render(request, 'liga/rosters.html', context)



def remaining(name, max):
    temp = Roster.objects.filter(owner__name=name).filter(athlete__kept=True)
    sum = 0
    for item in temp:
        sum = sum + item.athlete.price
    return max - sum

