"""

POO - Herança Múltipla 

- É a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde
todos os atributos e métodos de todas as classes herdadas.

#OBS:  A herança múltipla pode ser feita de duas maneiras:
    - Por multiderivação direta
    - Por multiderivação indireta
"""

# Exemplo 1 - Multiderivação direta
class Base1:
    pass 

class Base2:
    pass

class Base3:
    pass

class Multiderivacao(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação indireta
class Base1:
    pass 

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

# Exemplo 3

class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou o {self.__nome}"

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} Nadando..."

    def cumprimentar(self):
        return f"Eu sou o {self._Animal__nome} do mar"

class Terrestre(Animal):
    
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando"

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"

# Um animal que é tanto terrestre quanto aquático 
class Pinguim(Terrestre, Aquatico): # O que muda é pelo simples fato de trocar a ordem de herança aqui 
    
    def __init__(self, nome):
        super().__init__(nome)
    

# Testando
baleia = Aquatico("Wally")
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre("Xiquim")
print(tatu.andar())
print(tatu.cumprimentar())

pinguim = Pinguim("Mané")
print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar()) # MRO (Method Resolution Order)

# Objeto é instancia de...