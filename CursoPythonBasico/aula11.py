
lista = [1, 10]
try:
    divisao = 10 /1
    numero = lista[1]
    # x = a

except ZeroDivisionError:
    print('Não é possivel realizar uma divisão por: 0')
except IndexError:
    print('Erro ao acessar um indice invalido da lista:')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))

else:
    print('Não houve erro na execução:')

finally:
    print('Sempre Executa:')