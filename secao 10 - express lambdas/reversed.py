"""

reverse() -> é uma função própria para listas

"""

lista = [1, 2, 3, 4, 5]
print(lista)

"""
lista.reverse()
print(lista) 
"""


# Convertendo o elemento revertido para uma lista, tupla ou conjunto 
# Lista 
newlista = list(reversed(lista))
print(newlista)

# Tupla
tupla = tuple(reversed(lista))
print(tupla)

# Conjunto 
conj = set(reversed(lista))
print(conj)