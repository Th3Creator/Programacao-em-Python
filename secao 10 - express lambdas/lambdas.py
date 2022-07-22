"""

Expressões Lambdas: São basicamente funções que não possuem a necessidade de ter nome 
e colocar o return

Funções sem nome ou funções anônimas

"""

# Diferenciação entre uma função comum e uma expressão lambda

def funcaoempy(x):
    return 3 * x + 1
print(funcaoempy(10))

lambda x: 3 * x + 1
# Outra forma
calc = lambda x: 3 * x + 1
print(calc(10))
#obs: Antes dos ":" na expressão lambda seria equivalente ao parâmetro, após isso é tudo que vai retornar, que seria o return


# Exemplo 2
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
#obs: A função do stripe é deixar a letra inicial maiúscula e o title de deixar todas minúsculas
print(nome_completo('piSquIla', 'jHonEs'))

# Exemplo 3
amor = lambda: 'Como não amar Python'
print(amor())
#obs: também não é necessário possuir um parâmetro, pode passar nada no lugar e só colocar o retorno.