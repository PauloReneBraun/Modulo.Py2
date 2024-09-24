#Exemplo de herança 
from typing import Any

print("Exemplo de herança")
class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def falar(self) -> Any: