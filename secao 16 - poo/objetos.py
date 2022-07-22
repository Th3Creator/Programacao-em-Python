"""

POO - Objetos

- São instâncias das classes, ou seja, após o mapeamento do objeto do mundo real para a sua representação
computacional, devemos criar quantos objetos forem necessários. Objetos e Instâncias são a mesma cosia


"""

class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Usuario:
    def __init__(self, nome, email, senha):
        self.__nome = nome 
        self.__email = email
        self.__senha = senha


# Instanciando os Objetos

lamp1 = Lampada('Verde Florescente', 110, 60)

cc1 = ContaCorrente(5000, 2000)

user1 = Usuario("Chris sou Chris", "vinipvp@gmail.com", 654321)

# Minuto 12:32 ele fala sobre método de ligar e desligar lâmpada e verificar se está ligada ou desligada
