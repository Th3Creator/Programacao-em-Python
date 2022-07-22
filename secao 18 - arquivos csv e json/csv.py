"""

Lendo arquivos CSV

CSV - Comma Separeted Values - Valores separados por Vírgula

Podemos ter outros tipos de separadores e não somente a vírgula...

# Separados por vírgula 
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# Separador por ponto e vírgula 
1; 2; 3; 4; 5; 6; 7; 8; 9; 10


http://dados.gov.br/dataset
"""

with open('lutadores.csv') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

# Vai funcionar se estiver no mesmo diretório