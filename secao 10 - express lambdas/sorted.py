"""

Sorted

obs: Não confunda, apesar do nome, com a função sort() que já estudamos em Listas. 0 sort
só funciona em Listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve pra ordenar.

"""

numeros = [34, 9, 12, 18, 15, 3]
print(numeros)

newnumeros = sorted(numeros) #Ordena do menor para o maior
print(newnumeros) 

# Adicionano parâmetros no sorted 
newnumerosreverse = sorted(numeros, reverse=True) # Ordena do maior para o menor 
print(newnumerosreverse)

# No vídeo ele dá um ótimo exemplo usando o dicionário.