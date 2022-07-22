"""
- Utilizando list comprehensions nós podemos gerar novas listas com dados processados a partir de 
outro iterável.

Um tópico que retêm uma importância gigantesca e aconselhável fazer até duas vezes 
Ele é responsável pro pegar cada valor da lista e indo fazendo a alteração que o  programador definir

# Sintaxe da List Comprehensions

[dado for dado in interável]
"""

# Exemplo 1
numeros = [1, 2, 3, 4, 5]

resposta = [i * 10 for i in numeros]
# pega cada número da lista de números e mutiplica por 10
print(resposta)

"""
 Para entender sobre o que se trata a comprehensions, é necessário ter uma leitura de trás pra frente.
 Sendo para cada nummero(contador) dentro da lista de número, pegue o contador percorrendo e multiplique
 por cada posição que ele passar aquele elemento por 10
"""

# Exemplo 2
resposta2 = [ i / 2 for i in numeros]
print(resposta2)

# Diferenciação entre Loop e Comprehensions
# Usando o Loop
newnumerosdobrados = []

for i in [10, 11, 12, 13, 14, 15]:
    newnumerosdobrados.append(i * 2)

print(newnumerosdobrados)

# Comprehensions
print([i * 2 for i in [10, 11, 12, 13, 14, 15]])