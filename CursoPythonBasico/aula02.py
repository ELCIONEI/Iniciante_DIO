
a = int (input('Entre com o valor: '))
b = int (input('Entre com o valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

#print('soma: ' + str(soma))
#print('sobtracao: ' + str(subtracao))
#print('mutliplicacao: ' + str(multiplicacao))
#print('divisao:' + str(divisao))

print('Soma: {soma}. \nSubtracao: {sub}. '
      '\nMultiplicacao: {multi}'
      '\nDivisao: {div}'
      .format(soma=soma, sub=subtracao, multi=multiplicacao, div=divisao))