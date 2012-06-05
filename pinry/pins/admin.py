from django.contrib import admin
from pinry.pins.models import Pin , Movies


class PinAdmin(admin.ModelAdmin):
   pass

class MoviesAdmin(admin.ModelAdmin):
   pass

admin.site.register(Pin,PinAdmin)
admin.site.register(Movies,MoviesAdmin)


