#Pagina modelo padrao do Admim.

#imports
from django.contrib import admin
from core.models import Evento

#criando eventos na classe admim, será visualizado na tela do admin.
class EventoAdmin(admin.ModelAdmin):

     # visao da de tela admin.
    list_display = ('id','titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento')#filtro de pesquisa na tela admin.

#Associando o evento a classe.
admin.site.register(Evento, EventoAdmin)