from django.contrib import admin
from pinry.pins.models import Pin , Movies


class PinAdmin(admin.ModelAdmin):
   list_filter = ('movie','author',)
   search_fields = ['movie','author',]
   list_display = ('movie','author',)

class MoviesAdmin(admin.ModelAdmin):
   list_filter = ('name','year',)
   search_fields = ['name','description',]
   list_display = ('name','year',)

admin.site.register(Pin,PinAdmin)
admin.site.register(Movies,MoviesAdmin)


