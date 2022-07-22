"""

RANGES

- São utilizados para gerar sequências númericas, não de forma aleatória, mas
sim de maneira específicada.
"""

# Exemplo 1
for numeros in range(11):
    print(numeros)

# Exemplo 2
for numeros in range(1, 11):
    print(numeros)

# Exemplo 3
for numeros in range(5, 55, 2):
    print(numeros)
# OBS: valor de início, valor de parada, passo

# Exemplo 4
for numeros in range(5, 0, -1):
    print(numeros)
# OBS: agora é regressiva