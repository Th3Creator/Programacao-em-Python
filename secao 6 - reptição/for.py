"""

For

for item in interavel:
    ...

Exemplo de possíveis iteráveis:
- String 
    nome = "Chis sow Chris"
- Lista 
    lista = [1, 2, 3, 4, 5]
- Range 
    numero = range(1, 10)
"""

nome = "Chris sow Chris"
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)

# 1° For - Um for que itera sobre cada letra da variável nome
for letras in nome:
    print(letras)

# 2° for - Um for que itera sobre cada elemento da lista
for i in lista:
    print(i)

# 3° for - Um for que itera sobre um range
for r in range(1, 10):
    print(r)
#OBSERVAÇÃO: começa do 1 e vai até o 10, sendo que o valor final não é incluso no range