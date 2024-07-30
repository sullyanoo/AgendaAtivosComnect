from django.contrib import admin
from agenda.models import Evento

# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ("id","titulo", "data_evento", "data_criacao", "local") # Columns name admin template
    list_filter = ("usuario",) # dysplay filter admin template

admin.site.register(Evento, EventoAdmin)

