"""

POO - Métodos Mágicos

- São todos os métodos que utilizam dunder.

dunder init -> __init__

Dunder -> Double Underscore (Duplo Underline)

Seria meio que os métodos nativos da linguagem
"""
class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self) -> str:
        return f"{self.__titulo} escrito por {self.__autor}"
    # Seria meio que o toString

livro1 = Livro("Percy Jackson", "Irineu", 400)
livro2 = Livro("Harry Potter", "Pisquila", 500)   

print(livro1)
print(livro2)