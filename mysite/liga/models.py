from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=20)
    cap = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    position = models.CharField(max_length=3)
    kept = models.BooleanField()
    ftag = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Roster(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.name + ": " + self.athlete.name


class Trade(models.Model):
    tradeID = models.IntegerField()
    recipient = models.ForeignKey(Owner, on_delete=models.CASCADE)
    giver = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="givers")
    athlete = models.ForeignKey(Player, on_delete=models.CASCADE)
    cap = models.IntegerField(blank=True, null= True)

    def __str__(self):
        return "Trade " + str(self.tradeID) + ": " + self.giver.name + " gives " + self.athlete.name + " and $" + str(self.cap) + " to " + self.recipient.name
