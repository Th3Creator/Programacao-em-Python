"""

and, or, not, is

Operadores unitários:
    - not
Operadores binários:
    - and, or, is
"""

ativo = True
logado= False

if ativo:
    print("ele está ativo")
else:
    print("ele não está ativo")

# or 
if ativo or logado:  # Se um ou outro for verdadeiro o programa vai executar 
    print("Bem Vindo!")
else:
    print("ERROR!")

# and 
if ativo and logado:  # Os dois tem que ser verdadeiros para executar
    print("Bem Vindo!")
else:
    print("ERROR!")

# not
if not ativo:  # Se ele não for verdadeiro... execute isso
    print("Você precisa ativar a conta")
else:
    print("Bem vindo!")

# is 
if ativo is True:  # Se isso é aquilo... execute isso
    print("Bem Vindo!")
else:
    print("ERROR!")