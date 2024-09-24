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