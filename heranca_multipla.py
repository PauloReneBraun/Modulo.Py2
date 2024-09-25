class animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    def emitir_som(self):
        pass
    
class Reptil(animal):
    def SangueFrio(self):
        return f"{self.nome} Tem Sangue frio"
    
class Ave(animal):
    def voar(self):
        return f"{self.nome} Pode voar"
    
class Pterodactilo(Reptil, Ave):
    def emitir_som(self):
        super().emitir_som()
        return "Emitem Sons Altos e Estridentes"
    
pterodactilo = Pterodactilo(nome ="fantasma do pterodactilo Original")

# Acessando métodos da classe Pterodáctilo
print("Nome do pterodactilo:", pterodactilo.nome)
print("Pterodactilo emite som:", pterodactilo.emitir_som())