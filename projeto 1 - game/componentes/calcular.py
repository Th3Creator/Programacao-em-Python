from random import randint

class Calcular:

    def __init__(self, dificuldade: int) -> None: # Essa setinha indica o tipo de retorno
        self.__dificuldade: int = dificuldade

        # Atributos
        self.__valor1: int = self._gerarValor
        self.__valor2: int = self._gerarValor
        self.__operacao: int = randint(1, 3) # Vai criar um valor aleatório entre 1 a 3
        self.__resultado: int = self._gerarResultado
    
    # Encapsulamento 
    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade
    
    @property
    def valor1(self: object) -> int:
        return self.__valor1 

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ""

        if self.operacao == 1:
            op = "Somar"
        elif self.__operacao == 2:
            op = "Diminuir"
        elif self.__operacao == 3:
            op = "Multiplicar"
        else:
            op = "Operacao Desconhecida"
        return f"Valor 1: {self.__valor1} \nValor 2: {self.__valor2} \n Dificuldade: {self.__dificuldade} \nOperacação: {op}"

    # Métodos
    @property
    def _gerarValor(self: object) -> int:
        """ O retorno de dessa função irá ser o resultado de valor1 e valor2"""
        if self.dificuldade  == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return 0  

    @property
    def _gerarResultado(self: object) -> int:
        if self.operacao == 1: # Somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2        

    @property
    def opSimbolo(self: object) -> str:
        if self.operacao == 1:
            return "+"
        elif self.operacao == 2:
            return "-"
        else:
            return "*"

    def checarResultado(self: object, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print("Resposta correta!")
            certo = True
        else:
            print("Resposta errada")
        print(f"{self.valor1} {self.opSimbolo} {self.valor2} = {self.resultado}")
        return certo

    def mostrarOperacao(self: object) -> None:
        if self.operacao == 1:
            print(f"{self.valor1} {self.opSimbolo} {self.valor2}")

    
