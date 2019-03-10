from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from liga.models import Owner
from liga.models import Player
from liga.models import Roster
from django.template import loader
from django.urls import reverse


##########
#                Calculates franchise tag price
##########
def average(keeper_list):
    sum = 0
    iter = 0
    for item in keeper_list:
        sum = sum + Player.objects.get(pk=item).price
        iter = iter + 1
        if iter >= 5:
            break
    return int(sum/iter)


##########
#                Update all 4 Franchise Tag Prices
##########
def update_all_tags():
    positions= ["QB", "RB", "WR", "TE"]
    for item in positions:
        update_franchise_tag(item)


##########
#                Update the Franchise Tag for parameter position
##########
def update_franchise_tag(pos):
    # Get Franchise Tag Player
    tag_price_player = Player.objects.get(name__exact=pos + " Franchise")
    # Queryset of all kept players at position
    kept_players = Player.objects.filter(position=pos, kept=True).exclude(name__contains='Franchise').order_by('-price')

    # Get list of PKs
    kept_list = []
    for player in kept_players:
        kept_list.append(player.pk)

    # Change franchise tag price
    avg = average(kept_list)
    tag_price_player.price = avg
    tag_price_player.save()
