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

obj = MinhaClasse(nome="Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)