"""

Try / Except (try / cacth)

Reponsável por tratar erros que podem acontecer no nosso código. Previnindo assim que o o programa
pare de funcionar e o usuário receba mensagem de erro inesperados...

try:
    // execução do problema
except:
    // o que deve ser feito caso dê alguma problema
"""

# Tratando um erro genérico
try:
    geek()
except:
    print("Deu ruim menor")

print("Programa voltando...")

# Tratando um erro em específico
try:
    geek()
except NameError: #Se acontecer qualquer outro tipo de erro além desse ele não vai conseguir tratar
    print("Deu ruim menor")

print("Programa voltando...")

# no minuto 26:07 ele dá um ótimo exemplo de tratamento de exceção em funções