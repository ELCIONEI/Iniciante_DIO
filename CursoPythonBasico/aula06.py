
conjunto = {1, 2, 3, 4, 5, 4, 2}
conjunto2 = {6, 2, 5, 4, 9, 4, 2}
conjunto_uniao = conjunto.union(conjunto2)

print('União: {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecação: {}' .format(conjunto_interseccao))
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferença: {}'.format(conjunto_diferenca))

conjunto_a = {1, 2, 3, }
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjunto de A: {}'.format(conjunto_superset))

lista = ['lobo', 'cachorro', 'gato', 'elefante', 'arara']
print(lista)

conjunto_animais = set(lista)
print(conjunto_animais)


# conjunto = {1, 2, 3, 4, 5, 4, 2}
# conjunto.add (5)
# conjunto.discard(2)
# print(conjunto)
