from django.db import models
from django.contrib.auth.models import User # Import Django table users
# from datetime import datetime, timedelta

# Create your models here.

# Event table 

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now=True)
    local = models.CharField(blank=True, max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento' # Change the table title

    def __str__(self):
        return self.titulo # Returns the title in the table admin template 
    
    def get_data_evento(self): # Format my date time for default "dd/mm/aa hh:mm"
        return self.data_evento.strftime('%d/%m/%Y %H:%M')
    
    #def get_data_input_evento(self):
     #   return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    
    #def get_evento_atrasado(self):
     #   if self.data_evento < datetime.now():
      #      return True
       # else:
        #    return False