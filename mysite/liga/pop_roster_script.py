from liga.models import Player, Roster, Owner


p = Player.objects.get(name= 'Russell Wilson')
o = Owner.objects.get(name='Kevin')
r = Roster(owner=o, athlete=p)

r.save()
