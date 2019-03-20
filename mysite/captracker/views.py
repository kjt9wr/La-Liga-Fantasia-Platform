from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse

from liga.models import Owner
from liga.models import Trade
from liga.models import Player
from liga.models import Roster
from django.template import loader


##########
# #              Render Cap Tracker Page
##########
def captracker(request):
    owner_list = Owner.objects.all()
    trades = Trade.objects.all()
    cap_movements = Trade.objects.filter(cap__isnull=False)
    cap_exchange = []

    for trade in cap_movements:
        curr = parse_cap_trade(trade.tradeID, trade.recipient, trade.giver, trade.cap)
        cap_exchange.append(curr)

    context = {
        'owner_list': owner_list,
        'trades': trades,
        'cap_exchange': cap_exchange,
    }
    return render(request, 'captracker/captracker.html', context)

##########
# #              Render View Trade Page
##########
def viewTrade(request, tid):
    owner_list = Owner.objects.all()
    trades = Trade.objects.filter(tradeID=tid)
    full_trade = parse_full_trade(trades)

    parse_full_trade(trades)
    context = {
        'owner_list': owner_list,
        'tid': tid,
        'trade': full_trade,
    }
    return render(request, 'captracker/viewTrade.html', context)


##########
# #              Render Add Trade Page
##########
def addTrade(request):
    owner_list = Owner.objects.all()
    all_players = Player.objects.exclude(name__contains='Franchise').order_by('name')
    rosters_list = Roster.objects.all()
    context = {
        'owner_list': owner_list,
        'rosters_list' : rosters_list,
    }
    return render(request, 'captracker/addTrade.html', context)


##########
# #
# #              Returns [tid, {'owner': <Owner>, 'cap_rec': cap_received}, {'owner': <Owner>, 'cap_rec': cap_received}]
# #
##########
def parse_cap_trade(tid, f_owner, s_owner, cap):
    f_owner = owner_recs(f_owner, cap)
    s_owner = owner_recs(s_owner, cap*-1)
    my_trade = [tid, f_owner, s_owner]
    return my_trade


##########
# #              Returns Dictionary of owner key and cap received
##########
def owner_recs(owner, cap_received):
    dict1 = {
        'owner': owner,
        'cap_rec': cap_received,
    }
    return dict1


##########
# #              Returns Array of 2 Dicts:
# #                 [{   owner: <Owner>
# #                     cap: num
# #                     players_received: [<Player1> , <Player2>, ...]
# #                 }, ...]
##########
def parse_full_trade(trade_items):
    full_trade = []
    first = 0

    # Everything first owner receives
    dict1 = {}
    p1_recs = []

    # Everything second owner receives
    dict2 = {}
    p2_recs = []

    for asset in trade_items:
        if first == 0:
            dict1['owner'] = asset.recipient
            dict2['owner'] = asset.giver
            dict1['cap_rec'] = asset.cap
            dict2['cap_rec'] = asset.cap * -1
            first += 1

        # if owner1 is recipient
        if asset.recipient == dict1['owner']:
            p1_recs.append(asset.athlete)
        else:
            p2_recs.append(asset.athlete)

    dict1['players_received'] = p1_recs
    dict2['players_received'] = p2_recs
    full_trade.append(dict1)
    full_trade.append(dict2)
    return full_trade


##########
#                FORM: Add Trade
##########

def submit(request):
    trade = Trade.objects.all().order_by('-tradeID')
    new_tradeID = trade[0].tradeID + 1

    fcap = getInt(request, 'o1_cap')
    second = fcap == 0
    owner2 = Owner.objects.get(pk=request.POST.get('owner2'))
    owner1 = Owner.objects.get(pk=request.POST.get('owner1'))
    player_to_o1 = Player.objects.get(pk=request.POST.get('player1'))
    player_to_o2 = Player.objects.get(pk=request.POST.get('player2'))
    cap_rec = fcap
    # give_cap = True
    if second:
        cap_rec = getInt(request, 'o2_cap')
        t1 = Trade(tradeID=new_tradeID, recipient=owner2, giver=owner1, athlete=player_to_o2)
        t2 = Trade(tradeID=new_tradeID, recipient=owner1, giver=owner2, athlete=player_to_o1)
    else:
        t2 = Trade(tradeID=new_tradeID, recipient=owner2, giver=owner1, athlete=player_to_o2)
        t1 = Trade(tradeID=new_tradeID, recipient=owner1, giver=owner2, athlete=player_to_o1)
    t1.cap = cap_rec
    t1.save()
    t2.save()

    return HttpResponseRedirect(reverse('captracker:captracker'))


##########
#                Returns string as int
##########
def getInt(request, which):
    num = request.POST.get(which)
    if num == '':
        mynum = 0
    else:
        mynum = int(num)
    return mynum
