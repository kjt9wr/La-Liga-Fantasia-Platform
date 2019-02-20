print("from liga.models import Player, Roster, Owner")

with open('roster_list') as fp:
    for line in fp:
        x = line.split()
        print("p = Player.objects.get(name= '" + x[1] + " " + x[2] + "')")
        print("o = Owner.objects.get(name= '" + x[0] + "')")
        print("r = Roster(owner=o, athlete=p)")
        print("r.save() \n")




