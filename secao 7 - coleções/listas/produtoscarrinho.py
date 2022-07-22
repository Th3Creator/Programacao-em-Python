"""

Exemplo utilizando o conteúdo de listas, while e for

"""

carrinho = []
produtos = ''

while produtos != 'sair':
    print("Adiciona os produtos ou digite 'sair' para sair: ")
    produtos = input()
    if produtos != 'sair':
        carrinho.append(produtos)

for i in carrinho:
    print(i)