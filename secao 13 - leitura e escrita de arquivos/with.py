"""

Bloco With

- Utlizado para criar um contexto de trabalho, responsável por fechar o arquivo. O qual os recursos
utlizados são fechados após o bloco with.
"""

with open('texto.txt') as arquivo: # esse as significa nomear o que vem atrás com o que vem em seguida do 'as'
    print(arquivo.readlines())