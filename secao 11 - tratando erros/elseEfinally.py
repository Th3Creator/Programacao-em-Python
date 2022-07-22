"""

Else & Finally

Dica de quando e onde tratar o código:

TODA ENTRADA DEVE SER TRATADA!

"A função do usuário é destruir o seu sistema"
" você é responsável pela entrada das suas funções, o tratamento de erros dentro da sua função"

else -> só vai ser passado por ele caso não ocorra nenhum erro

finally -> diferentemente do else, ele vai ser sepre executável independete se tem erro ou não
"""

# Utilizando o else
try:
    numero = int(input("Digite um número:\n"))
except ValueError:
    print("Valor incorreto")
else:
    print(f"\nVocê digitou esse número: {numero}")


# Utilizando o finally
try:
    numero = int(input("Digite um número:\n"))
except ValueError:
    print("Valor incorreto")
else:
    print(f"\nVocê digitou esse número: {numero}")
finally:
    print("passou da mesma forma...")
# É utilizado para fechar ou desalocar recurso... utilizado bastante no banco de dados

# No minuto 32:12 ele dá um belo exemplo de tratando erros dentro da própria função...
# No minuto 37:04 uma forma bem legal refatorada desse mesmo código...