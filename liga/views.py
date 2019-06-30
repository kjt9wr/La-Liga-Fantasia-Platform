from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Owner
from .models import Player
from .models import Roster
from django.urls import reverse
from .functions import update_all_tags, keeper_update


def index(request):
    context = {}
    return render(request, 'liga/index.html', context)


##########
#                Render Rosters Page
##########
def rosters(request, owner_id):
    roster_items = Roster.objects.all()

    ownership = Roster.objects.filter(owner__pk=owner_id)
    owner_name = Owner.objects.filter(pk=owner_id).values('name')[0]['name']
    max_cap = Owner.objects.filter(pk=owner_id).values('cap')[0]['cap']
    rem_cap = remaining(owner_name, max_cap)

    context = {
        'roster_items': roster_items,
        'ownership': ownership,
        'max_cap': max_cap,
        'owner_name': owner_name,
        'owner_id': owner_id,
        'rem_cap': rem_cap,
    }
    return render(request, 'liga/rosters.html', context)


##########
#                Returns the owner's remaining cap based on max cap and kept players
##########
def remaining(name, max):
    temp = Roster.objects.filter(owner__name=name).filter(athlete__kept=True)
    sum = 0
    for item in temp:
        # Account for Franchise Tag
        if item.athlete.ftag:
            pos = item.athlete.position
            tag_price_player = Player.objects.get(name__exact=pos + " Franchise")
            sum = sum + tag_price_player.price
        else:
            sum = sum + item.athlete.price
    return max - sum


##########
#                FORM: Updates the player's kept attribute
##########
def update(request, owner_id):
    owner = Owner.objects.get(pk=owner_id)
    player_id_list = request.POST.getlist('item')
    ftagged = request.POST.get('franchise')
    not_kept = Roster.objects.filter(owner_id=owner.id)

    # Defaults all to false
    for each_player in not_kept:
        each_player.athlete.kept = False
        each_player.athlete.ftag = False
        each_player.athlete.save()

    # Change checked to True
    keeper_update(player_id_list)

    # Manage franchise tag
    if ftagged:
        tagged_player = Player.objects.get(pk=ftagged)
        tagged_player.ftag = True
        tagged_player.kept = True
        tagged_player.save()

    update_all_tags()
    return HttpResponseRedirect(reverse('liga:rosters', args=(owner.id,)))
