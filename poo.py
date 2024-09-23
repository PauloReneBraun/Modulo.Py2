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
print("Nome:",pessoa1.nome)
print("Idade:",pessoa1.idade)

pessoa2 = Pessoa('Maria', 30)
print("Nome:",pessoa2.nome)
print("Idade:",pessoa2.idade)