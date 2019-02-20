from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from liga.models import Owner
from liga.models import Player
from liga.models import Roster
from django.template import loader



def franchise(request):
    player_list = Player.objects.filter(kept=True)
    template = loader.get_template('franchise/franchise.html')
    context = {
        'player_list': player_list,
    }
    return HttpResponse(template.render(context, request))