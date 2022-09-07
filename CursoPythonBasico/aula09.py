import shutil
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
     arquivo = open(nome_arquivo, 'a')
     arquivo.write(texto)
     arquivo.close()

# def atualizar_arquivo(texto):
#     arquivo = open('teste.txt', 'a')
#     arquivo.write(texto)
#     arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_notas = arquivo.read()
    # print(aluno_notas)
    aluno_notas = aluno_notas.split('\n')
    # print(aluno_notas)
    lista_media = []

    for x in aluno_notas:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        # print(x)

def copia_arquivo(nome_arquivo):
    #import shutil
    shutil.copy(nome_arquivo, 'C:/Nova pasta')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'c:/')#colocar o endereço do arquivo

if __name__ == '__main__':
    #move_arquivo('notas.txt')
    #copia_arquivo('notas.txt')
    lista_media = media_notas('notas.txt')
    # print(lista_media)
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo ('teste.txt')
    # escrever_arquivo('minha primeira linha.\n')
# arquivo = open('teste.txt', 'a')
# arquivo.write(' Minha primeira linha')
# arquivo.write(' \n Minha segunda linha')
# arquivo.write(' \n Minha terceira linha')
# arquivo.close()
