from django.contrib import admin

from .models import Owner
from .models import Player
from .models import Roster

admin.site.register(Owner)
admin.site.register(Player)
admin.site.register(Roster)