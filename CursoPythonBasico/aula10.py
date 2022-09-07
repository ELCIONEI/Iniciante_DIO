from datetime import date, time, datetime


def trabalhadno_com_Datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('Data: %d/%m/%Y \nHoraLocal: %H:%M:%S'))
    print(data_atual.strftime('%c')) #Retorna dia,mes,ano,horalocal
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])


def trabalhando_com_date():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.minute)


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)


if __name__ == '__main__':
    trabalhadno_com_Datetime()
    # trabalhando_com_time()
    # trabalhando_com_date()
# data_atual = date.today()
# print(data_atual.strftime('%d/%m/%y'))

