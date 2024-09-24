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