#Exemplo de herança 
from typing import Any

print("Exemplo de herança")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self) -> Any:
        return f'{self.nome} está andando'
    def emitir_som(self) -> Any:
        return f'{self.nome} está emitindo som'
    
class Cachorro(Animal):
    def __init__(self, nome, raca) -> None:
        super().__init__(nome)
        self.raca = raca

    def latir(self) -> Any:
        return f'{self.nome} está latindo'
    
class Gato(Animal):
    def __init__(self, nome, cor) -> None:
        super().__init__(nome)
        self.cor = cor

    def miar(self) -> Any:
        return f'{self.nome} está miando'
    
dog = Cachorro('Tobias', 'Caramelo')
cat = Gato('Frajola', 'Branco')

print("\nExemplo de polimorfismo")
animals = [dog, cat] 
for animal in animais:
    print(f"{animal.nome} está emitindo som: {animal.emitir_som()}")

print("\nExemplo de encapsulamento")
class ContaBancaria:
    def __init__(self, nome, saldo) -> None:
        self.nome = nome
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f'{self.nome} depositou R${valor}'
        

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return f'{self.nome} sacou R${valor}'
        return f'Saldo insuficiente'
    
    def consultar_saldo(self):
        return self.__saldo