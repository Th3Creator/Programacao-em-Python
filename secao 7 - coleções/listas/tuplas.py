"""

Tuplas possuem uma certa semelhança com listas.

Existem praticamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()
2 - São imutáveis, ou seja, ao criar uma tupla ela não muda
"""

#Ambos os exemplos abaixo são considerados tuplas

tupla1 = (1, 2, 3, 4, 5)
tuplas2 = 1, 2, 3, 4, 5

# Não existe tuplas apenas com um elemento

tupla3 = (1) # Isso não é uma tupla
tupla4 = (1,) # Isso é uma tupla

# Gerando tuplas através de um range

tupla5 = tuple(range(11))

#  Desempacotamento de Tupla

tuplaname = ('Christian', 'Louzada')
nome, sobrenome = tuplaname

print(nome)
print(sobrenome)

# Contatenação de Tuplas

tupla6 = (6, 5, 4, 3, 2, 1)
tupla7 = (1, 2, 3, 4, 5, 6)

print(tupla6 + tupla7)

# iterando sobre uma Tupla
tuplaiterada = ('posicaoum', 'posicaodois', 'posicaotres')

for indice, valor in enumerate(tuplaiterada):
    print(indice, valor)

#Contando elementos dentro de uma Tupla
tuplacontudora = ('a', 'f', 'g', 'k', 'a', 'a')
print(tuplacontudora.count('a')) # Quantos elementos do parâmetro count possuem na tupla

