print("from liga.models import Player")

with open('player_list') as fp:
    for line in fp:
        x = line.split()
        x[1].replace("'", "")
        print("p = Player(name= '" + x[1] + " " + x[2] + "', price= " + x[3] + ", position = '" + x[4] + "', kept = True )\n")
        print("p.save()")
