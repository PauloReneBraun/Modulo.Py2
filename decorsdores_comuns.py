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