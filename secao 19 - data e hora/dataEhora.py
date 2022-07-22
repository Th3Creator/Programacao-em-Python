"""

Manipulando Data e Hora

- O python por si só já tem um built-in já integrado para poder trabalhar com data e hora chamado 
datetime
"""
import datetime

print(datetime.datetime.now())

# Outra forma de ser impresso 
print(repr(datetime.datetime.now()))

# Alterando o horário 
inicio = datetime.datetime.now()
alteracao = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(alteracao)


# Criando um data hora
nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")
print(nascimento)

nascimento = nascimento.split('/')

print(nascimento)
print(type(nascimento))

nascimento = datetime.datetime(int(nascimento[2], int(nascimento[1]), int(nascimento[0])))
