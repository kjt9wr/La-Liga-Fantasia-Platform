from django.shortcuts import render
from django.http import HttpResponseRedirect
from liga.models import Player
from django.urls import reverse
from liga.functions import update_franchise_tag, keeper_update


##########
#                Render Franchise Tag Page
##########
def available(request):

    context = {

    }
    return render(request, 'available/available.html', context)
