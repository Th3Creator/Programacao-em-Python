"""
Reduce

Guido Van (Criador da linguagem Python): Utilize a função reduce() se você realmente precisa dela. Em todo
caso, 99% das vezes em um loop for é mais legível.

Entendendo o reduce()

# Primeiro é necessário que tenha uma coleção de dados
dados = [a1, a2, a3, a4, a5]

# Depois é necessário ter uma função que contenha dois parâmetros
def function (x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável 
assi como no map e no filter.

reduce(funcao, dados)
"""
from functools import reduce


# Exemplo 1
dados = [2, 3, 4, 5, 13, 19, 20, 23, 29, 33]

multi = lambda x, y: x * y

resultado = reduce(multi, dados)
print(resultado)
#obs: ele vai guardando os valores e fazendo o somatório 
