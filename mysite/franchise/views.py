from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from liga.models import Owner
from liga.models import Player
from liga.models import Roster
from django.template import loader
from django.urls import reverse
from liga.functions import update_franchise_tag, keeper_update


##########
#                Render Franchise Tag Page
##########
def franchise(request):
    qb_list = get_list("QB")
    rb_list = get_list("RB")
    wr_list = get_list("WR")
    te_list = get_list("TE")
    tag_prices = []
    for i in range(4):
        tag_prices.append(Player.objects.filter(name__contains='Franchise').values('price')[i]['price'])
    context = {
        'qb_list': qb_list,
        'rb_list': rb_list,
        'wr_list': wr_list,
        'te_list': te_list,
        'tag_prices': tag_prices,
    }
    return render(request, 'franchise/franchise.html', context)


##########
#                FORM: Update the Franchise Tag Price
##########
def update(request, position):
    list = get_list(position)
    kept_list = request.POST.getlist('item')

    for player in list:
        player.kept = False
        player.save()

    keeper_update(kept_list)
    update_franchise_tag(position)
    return HttpResponseRedirect(reverse('franchise:index'))


##########
#                Returns queryset of players filtered by specific position
##########
def get_list(position):
    if position == "QB" or position == "TE":
        return Player.objects.filter(position=position).exclude(name__contains='Franchise').order_by('-price')
    else:
        return Player.objects.filter(position=position).exclude(name__contains='Franchise').filter(
            price__gte=20).order_by('-price')
