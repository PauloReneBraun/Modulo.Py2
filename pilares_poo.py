#Exemplo de herança 
from typing import Any

print("Exemplo de heranca")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self) -> Any:
        return f'{self.nome} esta andando'
    def emitir_som(self) -> Any:
        return f'{self.nome} esta emitindo som'
    
class Cachorro(Animal):
    def __init__(self, nome, raca) -> None:
        super().__init__(nome)
        self.raca = raca

    def latir(self) -> Any:
        return f'{self.nome} esta latindo'
    
class Gato(Animal):
    def __init__(self, nome, cor) -> None:
        super().__init__(nome)
        self.cor = cor

    def miar(self) -> Any:
        return f'{self.nome} esta miando'
    
dog = Cachorro('Tobias', 'Caramelo')
cat = Gato('Frajola', 'Branco')

print("\nExemplo de polimorfismo")
animals = [dog, cat] 
for animal in animals:
    print(f"{animal.nome} esta emitindo som: {animal.emitir_som()}")

print("\nExemplo de encapsulamento")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(saldo= 8000)
print(f"Saldo atual: {conta.consultar_saldo()}")
conta.depositar(valor=1000)
print(f"Saldo atual: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"Saldo atual: {conta.consultar_saldo()}")
conta.sacar(valor=1000)
print(f"Saldo atual: {conta.consultar_saldo()}")

conta_do_luizinho = ContaBancaria(saldo= 20)

print("\nExemplo de abstracao")
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
class Moto(Veiculo):
    def __init__(self) -> None:
        pass
    
    def ligar(self):
        return 'Moto ligada'
    
    def desligar(self):
        return 'Moto desligada'
    
Moto_Preta =  Moto()
print(Moto_Preta.ligar())
print(Moto_Preta.desligar())