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
    def get_arma(self):
        return self.__arma
    
    def get_poder(self):
        return self.__poder