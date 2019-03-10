from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from liga.models import Owner
from liga.models import Player
from liga.models import Roster
from django.template import loader
from django.urls import reverse


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
#                Update the Franchise Tag Price based on form
##########
def update(request, position):
    list = get_list(position)
    kept_list = request.POST.getlist('item')

    for player in list:
        player.kept = False
        player.save()

    for item in kept_list:
        selected_player = Player.objects.get(pk=item)
        selected_player.kept = True
        selected_player.save()

    franchise_tag = Player.objects.get(name__exact=position + " Franchise")
    avg = average(kept_list)
    franchise_tag.price = avg
    franchise_tag.save()
    print(avg)
    return HttpResponseRedirect(reverse('franchise:index'))



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
#                Returns queryset of players filtered by specific position
##########
def get_list(position):
    if position == "QB" or position == "TE":
        return Player.objects.filter(position=position).exclude(name__contains='Franchise').order_by('-price')
    else:
        return Player.objects.filter(position=position).exclude(name__contains='Franchise').filter(price__gte=20).order_by('-price')

