from django.shortcuts import render
from django.http import HttpResponse

from liga.models import Owner
from liga.models import Player
from liga.models import Roster
from django.template import loader


# Create your views here.


def captracker(request):
    owner_list = Owner.objects.all()
    template = loader.get_template('captracker/captracker.html')
    context = {
        'owner_list': owner_list,
    }
    return HttpResponse(template.render(context, request))
