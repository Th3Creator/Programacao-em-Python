"""

POO - Método Super 

- O método super() se refere a super classe, classe pai no caso

"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome 
        self.__especie = especie

    def fazSom(self, som):
        print(f"{self.__nome} faz {som}")

class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca
    

