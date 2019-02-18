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

    def __str__(self):
        return self.name

class Roster(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.name + ": " + self.athlete.name
