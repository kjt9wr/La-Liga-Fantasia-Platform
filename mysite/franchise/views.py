from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from liga.models import Owner
from liga.models import Player
from liga.models import Roster
from django.template import loader
from django.urls import reverse



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


def update(request, position):
    list = get_list(position)
    kept_list = request.POST.getlist('item')

    for player in list:
        player.kept = False
        player.save()

    print("\n\n")
    for item in kept_list:
        selected_player = Player.objects.get(pk=item)
        selected_player.kept = True
        selected_player.save()
    return HttpResponseRedirect(reverse('franchise:index'))



#def update(request, owner_id):
 #   owner = Owner.objects.get(pk=owner_id)
  #  player_id_list = request.POST.getlist('item')
 #   not_kept = Roster.objects.filter(owner_id=owner.id)

    #change unchecked to False
 #   for each_player in not_kept:
 #       each_player.athlete.kept = False
 #       each_player.athlete.save()

    #Change checked to True
 #   for player in player_id_list:
#        selected_player = Player.objects.get(pk=player)
  #      selected_player.kept = True
   #     selected_player.save()
    #return HttpResponseRedirect(reverse('liga:rosters', args=(owner.id,)))



def get_list(position):
    if position == "QB" or position == "TE":
        return Player.objects.filter(position=position).exclude(name__contains='Franchise').order_by('-price')
    else:
        return Player.objects.filter(position=position).exclude(name__contains='Franchise').filter(price__gte=20).order_by('-price')

