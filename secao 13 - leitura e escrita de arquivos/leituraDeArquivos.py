"""

Leitura de Arquivos

- Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utlização nós passamos apenas um parâmetro de entrada,
que neste caso é o nome do arquivo a ser lido. Essa função retorna um _io_ . TextIOWrapper 
e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open 

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir,
ou então teremos o erro FileNotFoundError.

mode r-> Significa modo de leitura. r -> vem do read(ler)

"""

arquivo = open('texto.txt')
# print(arquivo)

# Após aplicação da função open é necessário passar a função read()... caso deseja ler o arquivo

print(arquivo.read()) 