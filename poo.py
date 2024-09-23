# Poo

#classe exemplo 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos'

#Objeto
pessoa1 = Pessoa('João', 20)
print(pessoa1.saudacao())


pessoa2 = Pessoa('Maria', 30)
print(pessoa2.saudacao())
