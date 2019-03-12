from django.shortcuts import render
from django.http import HttpResponse

from liga.models import Owner
from liga.models import Trade
from liga.models import Player
from liga.models import Roster
from django.template import loader


# Create your views here.


def captracker(request):
    owner_list = Owner.objects.all()
    trades = Trade.objects.all()
    cap_exchange = []
    for trade in trades:
        curr = store_trade(trade.tradeID, trade.recipient.pk, trade.giver.pk, trade.cap)
        cap_exchange.append(curr)
    print(cap_exchange)
    context = {
        'owner_list': owner_list,
        'trades': trades,
        'cap_exchange': cap_exchange,
    }
    return render(request, 'captracker/captracker.html', context)


def viewTrade(request, tid):
    owner_list = Owner.objects.all()
    context = {
        'owner_list': owner_list,
        'tid': tid,
    }
    return render(request, 'captracker/viewTrade.html', context)


def addTrade(request):
    owner_list = Owner.objects.all()
    context = {
        'owner_list': owner_list,
    }
    return render(request, 'captracker/addTrade.html', context)


def store_trade(tid, f_owner_pk, s_owner_pk, cap):
    f_owner = owner_recs(f_owner_pk, cap)
    s_owner = owner_recs(s_owner_pk, cap*-1)
    my_trade = [tid, f_owner, s_owner]
    print(str(tid))
    return my_trade


def owner_recs(owner_pk, cap_received):
    dict1 = {
        'oid': owner_pk,
        'cap_rec': cap_received,
    }
    return dict1

# [{},{}]
# {   oid: num
#     cap rec: num
#     players rec: [pid1,pid2...]
#    }