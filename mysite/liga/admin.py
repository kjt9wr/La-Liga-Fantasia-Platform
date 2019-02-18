from django.contrib import admin

from .models import Owner
from .models import Player

admin.site.register(Owner)
admin.site.register(Player)
