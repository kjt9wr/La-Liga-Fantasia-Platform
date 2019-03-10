from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Owner
from .models import Player
from .models import Roster
from django.template import loader
from django.urls import reverse

def index(request):
    context = {}
    return render(request, 'liga/index.html', context)



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
        if item.athlete.ftag:
            print("Change value\n")
            pos = item.athlete.position
            tag_price_player = Player.objects.get(position=pos, name__contains='Franchise')
            tag_price = tag_price_player.price
            sum = sum + tag_price
        else:
            sum = sum + item.athlete.price
    return max - sum


##########
#                Updates the player's kept attribute
##########
def update(request, owner_id):
    owner = Owner.objects.get(pk=owner_id)
    player_id_list = request.POST.getlist('item')
    ftagged = request.POST.get('franchise')
    not_kept = Roster.objects.filter(owner_id=owner.id)


    #change unchecked to False
    for each_player in not_kept:
        each_player.athlete.kept = False
        each_player.athlete.ftag = False
        each_player.athlete.save()

    #Change checked to True
    for player in player_id_list:
        selected_player = Player.objects.get(pk=player)
        selected_player.kept = True
        selected_player.save()

    #Manage franchise tag
    if(ftagged):
        tagged_player = Player.objects.get(pk=ftagged)
        tagged_player.ftag = True
        tagged_player.kept = True
        print("Changing " + tagged_player.name + " to true")
        tagged_player.save()

    return HttpResponseRedirect(reverse('liga:rosters', args=(owner.id,)))


