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