# @classmethod
# @staticmethod

class MinhaClasse:
  def __init__(self, nome) -> None:
    self.nome = nome #Atributo da instância

  def metodo_instancia(self):
    return f"Metodo de instancia {self.nome}"
  
  @classmethod
  def metodo_classe(cls):
    return f"Metodo de classe {cls}"
  
  @staticmethod
  def metodo_estatico():
    return "Metodo estatico"

obj = MinhaClasse(nome="Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class moto:
  def __init__(self, marca, modelo, cor) -> None:
    self.marca = marca
    self.modelo = modelo
    self.cor = cor

  @classmethod
  def criar_moto(cls, configuracao):
    marca, modelo, cor = configuracao.split('-')
    return cls(marca, modelo, cor)
  
configuracao = "Honda-CB300-Preto"
moto1 = moto.criar_moto(configuracao)
print(moto1.marca)

class Matematica:
  @staticmethod
  def soma(a, b):
    return a + b

  @staticmethod
  def subtracao(a, b):
    return a - b