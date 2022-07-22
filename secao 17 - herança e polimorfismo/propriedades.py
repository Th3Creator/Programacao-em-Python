"""

POO - Propriedades

- Ensinando como encapsular os atributos 
"""

class Conta:
    contador = 0 

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo 
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor 

    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor
    
    def getNumero(self):
        return self.__numero
    
    def getTitular(self):
        return self.__titular
    
    def serTitular(self, titular):
        self.__titular= titular
    
    def getSaldo(self):
        return self.__saldo
    
    def getLimite(self):
        return self.__limite

conta1 = Conta("Chris sow Chris", 3000, 5000)
conta2 = Conta("Pisquila", 2000, 4000)

soma = conta1.getSaldo() + conta2.getSaldo()

print(soma)


# REFATORANDO O CÓDIGO
class Conta2:
    contador = 0 

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo 
        self.__limite = limite
        Conta.contador += 1
    
    # Encapsulamento
    @property
    def numero(self):
        return self.__numero
    
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    #cria um decoretor com o mesmo nome do atributo que deseja settar   

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    def extrato(self):
        return f"Saldo de {self.__saldo} do cliente {self.__titular}"

    def depositar(self, valor):
        self.__saldo += valor 

    def sacar(self, valor):
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

conta3 = Conta2("Chris sow Chris", 3000, 5000)
conta4 = Conta2("Pisquila", 2000, 4000)

soma2 = conta3.saldo + conta4.saldo
print(soma2)

"""
OBSERVAÇÕES:

- Observe que é so fazer assim conta.saldo que você pega o valor dele, e caso procure definir seria
a mesma coisa (caso tivesse o set é claro), seria conta.saldo = x(um valor aleatório)


"""