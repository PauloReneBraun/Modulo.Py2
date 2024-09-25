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
    
class pterodáctilo(Reptil, Ave):
    def emitir_som(self):
        super().emitir_som()
        return "Emitem Sons Altos e Estridentes"