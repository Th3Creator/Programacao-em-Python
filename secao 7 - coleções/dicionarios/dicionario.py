"""
Um mapeamento enter chave e valor

Sendo representados assim por {}.

E também os valores dentro das chaves podem ser de qualquer tipo
"""

# Exemplo 1
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguay'}
print(paises)

# Exemplo 2: Ambos podem ser escritos da mesma forma
paises2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguay') 
print(paises2)

# Acessando elementos
print(paises['BR'])

# Acessando via get (Que seria o recomendado)
print(paises.get('BR'))

# Tuplas por exemplo são bastante utilizadas como chaves de dicionários, até porquê são imutáveis
# Exemplo a seguir de latitude e longitude

localidades = {
    (35.685, 38.6917): 'Escritório em Tokio',
    (40.710, 74.8327): 'Escritório em Nova York',
    (37.470, 122.3087): 'Escritório em São Paulo'
}

print(localidades)

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}

receita['abr'] = 350
print(receita)
# E pra caso queira atualizar um dado dentro do dicionário, é a mesma coisa
# obs: Não podemos ter chaves repetidas

# Remover dados de um dicionário
receita.pop('mar') # Para remover é obrigatório passar a chave
print(receita)
# Outra forma
del receita['fev']
print(receita)

