"""

POO - Atributos

- Signfica às características de um objeto

Em Python dividimos os atributos em 3 grupos:
    - Atributos de Instâncias;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de instâncias: São atributos declarados dentro do método contrutor.
# OBS: Método contrutor: É um método especial utilizado para a construção do objeto.

EXEMPLO EM JAVA

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = falase;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}


"""

class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False
# OBS: Os atributos de instâncias a gente já declara dento do método construtor
# o método initit que é definido que o método construtor 
# o private em Python é o "__"

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha  

# Métodos são funções dentro de uma classe

"""

Self -> Vem do mesmo sentido de um restaurante self serive, uma metodologia de "auto serviço"

"""

# Atributos públicos ou privados, o que define um atributo ser privado é os dois underline no início 


# EXEMPLO 
class Acesso: 
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

user1 = Acesso("user@gmail.com", "4321")

print(user1.email)


# Atributos de Classes
class Produto:
    imposto = 1.05 # Ou seja, 0,05% de imposto

    def __init__(self,nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)


produto = Produto("TV", "200 polegadas", 5000)
produto2 = Produto("PlayStation", "Vídeo game", 2500)

print(produto.valor)
print(produto2.valor)

# No minuto 1:03:05 ele dá um ótimo exemplo de como utilizar o id nas classes...