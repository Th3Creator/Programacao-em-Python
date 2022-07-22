lista1 = ['Christian', 'Louzada']
lista2 = [1, 28, 90 , 45, 16, 18, 40, 36]
lista3 = list(range(11)) 
lista4 = list('Christian Louzada')

if 8 in lista3: #nessa o if faz com que o parâmetro passado passe por dentro da lista
    print('Está dentro da lista 3')
else:
    print('Não está dentro da lista 3')

# Nesse exemplo verificando uma lista que contem letras
if 'z' in lista4:
    print('Encontrou o z')