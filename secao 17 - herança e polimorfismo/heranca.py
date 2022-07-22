"""

POO - Herança 

- A ideia de herança é o reaproveitamento de código. Como também extender a nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe 
que passa a herdar atributos e métodos da classe herdada

OBS2: Quando uma classe herda de outra classe, ela herda todos os atributos e métodos da classe herdada
"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nomeCompleto(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa): # Isso é equivalente ao extendes de Java
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nomeCompleto(self):
        print(super().nomeCompleto())
        return f"{self.__matricula}"

# Sobrescrita de métodos...

cliente1 = Cliente("Christian", "Louzada" , "149" , 5000)
funcionario1 = Funcionario("Brenin", "Pirocopteo", "509", 1000)

print(cliente1.nomeCompleto())
print(funcionario1.nomeCompleto())