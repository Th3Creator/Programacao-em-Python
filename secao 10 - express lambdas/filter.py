"""

Filter (): Filtrar dados de uma determinada coleção 

"""
# Imporatando biblioteca que trabalha com estatísticas
import statistics

dados = [2, 3, 4, 5, 6, 7, 8]

media = statistics.mean(dados) #função mean é responsável por calcular a média dos dados
print(media)

# Utilizando o filter, sendo o filter recebendo dois parâmetros (uma função e um iterável)
resultado = filter(lambda x: x > media, dados)
"""
O filtro recebe a função lambda com o retorno só dos número que estão acima da media
e logo em seguida passa o iterável, que seria a determinada coleção, ele pega cada dado do 
iterável e passa como parâmetro da função lambda
"""
print(list(resultado)) #Sempre transformando em uma lista, sendo que os resultados de mapobj lá

#A diferença entre map e filter 

# A diferença é que no map retornar valores e no filter retornar ou true ou false

# Exemplo 2 de filter 

# Filter e Map