from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from liga.models import Owner
from liga.models import Player
from liga.models import Roster
from django.template import loader



def franchise(request):
    qb_list = Player.objects.filter(position="QB").order_by('-price').order_by('-price')
    rb_list = Player.objects.filter(position="RB").filter(price__gte=20).order_by('-price')
    wr_list = Player.objects.filter(position="WR").filter(price__gte=20).order_by('-price')
    te_list = Player.objects.filter(position="TE").order_by('-price').order_by('-price')
    context = {
        'qb_list': qb_list,
        'rb_list': rb_list,
        'wr_list': wr_list,
        'te_list': te_list,
    }
    return render(request, 'franchise/franchise.html', context)
