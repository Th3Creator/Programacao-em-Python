"""

Seek e Cursors

seek() -> É utlizada pra movimentar o cursor pelo arquivo.
"""


arquivo = open('texto.txt')
# print(arquivo)

# Após aplicação da função open é necessário passar a função read()... caso deseja ler o arquivo

print(arquivo.read()) 
# Movimentar o cursor pelo arquivo com a função seek
arquivo.seek(0)