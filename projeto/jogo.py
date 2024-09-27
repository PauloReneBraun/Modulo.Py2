#Personagem : classe Mae 
#Heroi : controlado pelo usuario 
#Inimigo : controlado pela IA 

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
    def get_nome(self):
        return self.__nome  
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
        self.__arma = 'Espada'
        self.__poder = 'Fogo'

    def get_habilidade(self):
        return self.__habilidade
    def get_arma(self):
        return self.__arma
    
    def get_poder(self):
        return self.__poder
    
    def exibir_detalhes(self):
        return f'Nome: {self.get_nome()} | Vida: {self.get_vida()} | Nível: {self.get_nivel()} | Habilidade: {self.get_habilidade()} | Arma: {self.get_arma()} | Poder: {self.get_poder()}'
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        self.__arma = 'Espada'
        self.__poder = 'Fogo'
        
    def get_tipo(self):
        return self.__tipo
    
    def get_arma(self):
        return self.__arma
    
    def get_poder(self):
        return self.__poder
    
    def exibir_detalhes(self):
        return f'Nome: {self.get_nome()} | Vida: {self.get_vida()} | Nível: {self.get_nivel()} | Tipo: {self.get_tipo()} | Arma: {self.get_arma()} | Poder: {self.get_poder()}'
    
Heroi1 = Heroi(nome='João', vida=100, nivel=1, habilidade='Voar')
print(Heroi1.exibir_detalhes())
inimigo1 = Inimigo(nome='Maria', vida=100, nivel=1, tipo='Zumbi')
print(inimigo1.exibir_detalhes())