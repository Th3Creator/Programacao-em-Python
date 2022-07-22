"""

While (enquanto)

"""


i = 0
while i < 11:
    print(i)
    i= i + 1

"""

OBS: O critério de parada no while é a condição passada se tornar falsa uma hora, caso
contrário o loop será infinito

"""

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica?')


"""

Break (parada)

- Utilizado para sair e loops de maneira projetada
"""

for numero in range(1, 11):
    if numero == 6:
        print("Chegou no 6")
        break
    else:
        print(numero)
print("SAIUU")

