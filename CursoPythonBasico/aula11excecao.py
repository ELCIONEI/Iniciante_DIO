class Error(Exception):
    pass

class ImputError(Error):
    def __int__(self, message):
        self.message = self(message)

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x >10:
            raise ImputError('Não pode ser maior que: 10')
        elif x < 0:
            raise ImputError('Não pode ser menor que: 0')
        break

    except ValueError:
        print('Valor invalido. Apenas numeros')
    except ImputError as ex:
        print(ex)