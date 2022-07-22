"""

Levantando os nossos próprios tipos de erros com o raise

raise -> lança exceções 

OBS: O raise não é uma função
Ele se torna útil para criarmos nossas próprias exceções e mensagens de erros

Forma geral de utilização do raise:

raise TipoDoErro("Mensagem de erro")

"""

def colore(texto, cor):
    cores = ('verde', 'azul', 'vermelhor')
    if type(texto) is not str:
        raise TypeError("O seu burro... isso não é uma string...")
    if type(cor) is not str:
        raise TypeError("O seu jumento... isso não é uma string...")
    if cor not in cores:
        raise TypeError("Essa cor não pertence ao conjunto de cores ofertados...")
    else:
        print("Tudo certo por aqui")

colore("BB", "azul")