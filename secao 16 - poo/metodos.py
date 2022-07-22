"""

POO - Métodos 

- Representa os comportamentos do objeto. Ou seja, às ações que esse objeto pode realizar no seu
sistema (funções).

Em Python, dividimos os métodos, assim como os atributos, em 2 grupos: Métodos de instância e
métodos de classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.



"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

class ContaCorrente:
    contador = 5000

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    
    def desconto(self, porcentagem):
        """ Retorna o valor do produto com o desconto"""
        return(self.__valor * (100 - porcentagem)) / 100
        
    

class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome 
        self.__email = email
        self.__senha = senha
    
    def correr(self, metros):
        print(f"O {self.__nome} correu {metros} metros em uma maratona")
    
    def sobrenome(self, sobrenome):
        return f"{self.__nome} {sobrenome}"

user1 = Usuario("Chris sou Chris", "carlinhospvp_mine@gmail.com", 1234)
user1.correr(10)
print(user1.sobrenome("Scoucô")) 

produto1 = Produto("Natacha", "Muitcho bom", 50)
print(produto1.desconto(50))