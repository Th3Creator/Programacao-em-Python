"""

Map: É uma função onde recebe dois parãmetros, sendo o primeiro a função e o segundo o interável 

"""

def area(r):
    return 3.14 * (r ** 2)

raios = [1, 20, 13, 83, 42, 64, 42]

# Utilizando o map

areas = map(area, raios)
#pegando cada elemento da lista raios e usando lá na função e depois adicioando os resultados em um Map Object
print(list(areas)) # É nessário passar de Map Object pra lista, pode também passar pra dicionário, tuplas etc.


# Também é possível utilizar o lambda junto com o Map 12:16

# E também no minuto 24:24 ele mostrando usando map junto com coleções + lambdas... Muito prático