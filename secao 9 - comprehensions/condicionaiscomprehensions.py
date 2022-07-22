"""

Usando as estruturas condicionais aplicadas em List Comprehensions

"""

# Exemplo usando uma lista de número e um comprehensions que verifica se é par ou impar

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [i for i in numeros if i % 2 == 0]
impares  = [i for i in numeros if i % 2 != 0]

print(pares)
print(impares)
