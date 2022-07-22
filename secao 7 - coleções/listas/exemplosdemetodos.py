# Listas para Testes 
lista1 = ['Christian', 'Louzada']
lista2 = [1, 28, 90 , 45, 16, 18, 40, 36]
lista3 = list(range(11)) 
lista4 = list('Christian Louzada')


# Exemplos do que é possivel fazer com listas 

# Vendo as opçõe que dá pra fazer com listas
print(dir(lista2)) #vai listar todos os métodos e propriedades que dá pra fazer com listas

# Através do dir encontra o método sort, que coloca em ordem os números 
lista2.sort()
print(lista2) 

# Através do count conseguimos contar o número de repetição de um elemento em uma lista
print(lista4.count('i')) # Quantidade de letras i dentro da lista 4

# Adicionando elementos em uma lista utilizando append
lista2.append(19)
print(lista2) #vendo se realmente adicionou na lista2
#obs: essa função append adiciona apenas um elemento
# No entanto podemos adicionar uma lista com mais de um elemento dentro de outra lista usando o append
lista2.append([20,60,70])
print(lista2)

# Diferentemente do append, o extend adiciona mais de um elemento em uma lista
lista2.extend([1, 2, 3])
print(lista2)

# Inserindo elementos agora informando a posição do indice na lista
lista2.insert(3, 23)
print(lista2)

# Saber a quantidade de elementos dentro de uma lista 
print(len(lista2))

# Com o pop você remove o último elemento, mas também consegue remover um elemento passando a sua posição no seu parâmetro
print(lista2.pop())
print(lista2.pop(3)) # Removendo o elemento na posição 3

