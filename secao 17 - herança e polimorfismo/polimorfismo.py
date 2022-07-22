"""

POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

- Objetos que podem possuir muitas formas
"""

class Animal(object):
    
    def __init__(self, nome):
        self.__nome = nome
    
    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este método")

    def comer(self):
        print(f"{self.__nome} está comendo")
    
class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} RUF RUF")
    
class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)
    
    def falar(self):
        print(f"{self.__Animal__nome} MIAUUUU MIAAAUUUU")

class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


# Testando o código
felix = Gato("Felix")
felix.comer()
felix.falar()

pluto = Cachorro("Pluto")
pluto.comer()
pluto.falar()

mickey = Rato("Mickey")
mickey.comer()
mickey.falar()

# Um mesmo animal pode possuir muitas formas