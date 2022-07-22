""" 
Utilitários de Python que lhe auxiliam na programação

Dir -> Apresenta todos os atributos e funções/métodos disponíveis para determinado tipo de variável.

ex: dir(tipo de dado/variável). Dando assim todos atributos, propriedades, funções e métodos.

Help ->Apresenta a documentação/como utilizar os atributos/propriedades e funnções/métodos disponíveis
para determinado  tipo de dado ou variável.

ex help(o que deseja descobrir). Retornando assim a documentação de como utilizar aquilo passado no parâmetro 
help.

"""




#Exemplos 
nome = "Christian"

print(dir(nome)) #Vai mostrar tudo que é possível ser feito.

#Logo após é que o help entra em ação, ele vai te auxiliar mostrando o que
#cada um daquelas coisas que apareceram fazem.

#Por exemplo
help(nome.lower) #Vai trazer a documentação daquilo selecionado

print(nome.lower()) #Que no caso deixa tudo minúsculo





"""

Então resumindo, através desses dois utilitários você consegue ver a documentação da linguagem python
e saber o que pode ser feito, meio que o prototype do JavaScript

"""