"""

Recebendo os dados do usuário

"""


"""
#Entrada de dados
print("Qual é o seu nome?")
nome = input() # Significa entrada em inglês, seria basicamente o scanner


#Entrada de dados com valores inteiros
print("\nDigite a sua idade:");
idade = int(input()) #O mesmo vale pro float, é so substituir ali no lugar do int
#OBSERVAÇÃO: TODAO DADO RECEBIDO DO INPUT É DO TIPO STRING, por isso é necessário a conversão

print("\nSeja bem vindo(a) {0}, sua idade e: {1}" .format(nome, idade))
"""

print("The king is back\n")

print("Digite o nome do lutador n1:")
lutador_n1 = input()

print("Digite o nome do lutador n2:")
lutador_n2 = input()

# As outras duas maneiras de dar print com o valor das variáveis 
print("{0} contra {1}" .format(lutador_n1, lutador_n2))
# ou
print(f"{lutador_n1} contra {lutador_n2}")

#ou até mesmo assim ó... Bem melhor
lutador_n3 = input("Qual o seu nome guerreiro: ")
lutador_n4 = input("Seu nome cumpadi: ")
print(f"{lutador_n3} contra {lutador_n4}")

"""
Por padrão o input sempre vai receber um dado do tipo string, por isos é necessário fazer o cast
e passar essa conversão, tanto pra int quanto pra float
"""