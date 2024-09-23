# Poo

#classe exemplo 
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

#Objeto
pessoa1 = Pessoa('João', 20)