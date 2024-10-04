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

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = self.__nivel * 2
        print(f'O herói {self.get_nome()} atacou o inimigo {alvo.get_nome()} e causou {dano} de dano.')

    
  
    
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
    

    def ataque_especial(self, alvo):
        dano = self.__nivel * 5
        alvo.receber_dano(dano)
        print(f'{self.get_nome()} usou habilidade especial {self.get_nome()} e causou {dano} de dano.')
    class Jogo:
        """Classe para representar o jogo"""
        def __init__(self):
            self.heroi =Heroi(nome='João', vida=100, nivel=1, habilidade='Voar')
            self.inimigo = Inimigo(nome='Maria', vida=100, nivel=1, tipo='Zumbi')
            self.__personagens = []
            
        def iniciar_jogo(self):
            """Método para controle de batalha"""
            print('O jogo começou!')
            while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
                print("\nDetalhes do herói:")
                print(self.heroi.exibir_detalhes())
                print("\nDetalhes do inimigo:")
                print(self.inimigo.exibir_detalhes())

                input("\nPressione Enter para atacar o inimigo...")
                escolha = input("Escolha o ataque (1 - Fogo, 2 - Gelo, 3 - Raio): ")    
                if escolha == '1':
                    self.heroi.atacar(self.inimigo)
                elif escolha == '2':
                    self.heroi.ataque_especial(self.inimigo)
                else:
                    print('Ataque inválido!')



                if self.inimigo.get_vida() > 0:
                    #iNIMIGO ATACA IO HEROI
                    self.inimigo.atacar(self.heroi)
            if self.heroi.get_vida() > 0:
                print('O herói venceu a batalha!')
            else:
                print('O inimigo venceu a batalha!')
    

#Criação de jogo e inicio de batalha 
jogo = Jogo()
jogo.iniciar_jogo()
Heroi1 = Heroi(nome='João', vida=100, nivel=1, habilidade='Voar')
print(Heroi1.exibir_detalhes())
inimigo1 = Inimigo(nome='Maria', vida=100, nivel=1, tipo='Zumbi')
print(inimigo1.exibir_detalhes())