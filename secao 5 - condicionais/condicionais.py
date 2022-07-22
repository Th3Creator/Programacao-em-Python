"""

Condicionais beath!!!

"""
print("Sendo a tabela dividida da seguinte forma:\n 1)SE sua idade for menor que 18 anos = adolescente\n 2)SE sua idade for maior que 18 anos = adulto\n 3)E se sua idade for menor que 12 anos = criança")

print("\nDigite a sua idade:")
idade = int(input())

if idade >= 12 and idade <= 18:
    print("\nvoce e um aborrecente")
elif idade > 18: 
    print("\nvoce e um adulto responsavel")
elif idade < 12:
    print("\nvoce e uma criança")