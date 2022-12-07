#Area de criação de tabelas.
from django.db import models #importar modelo de bancos de dados.
from django.contrib.auth.models import User #importar  modelo de tabela usurio.

#Criando a tabela da agenda.
class Evento(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)#branco ou nulo.
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)#registra a hora atual.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)#deleta tudo do usuario.

    class Meta:#para forçar o banco aceitar o nome escolhido.
        db_table = 'evento'

    #para retornar os eventos dos usuarios.
    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M:%S')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y/%m/%dT%H:%M')

