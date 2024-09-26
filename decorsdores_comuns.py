# @classmethod
# @staticmethod

class MinhaClasse:
  def __init__(self, nome) -> None:
    self.nome = nome #Atributo da instância

  def metodo_instancia(self):
    return f"Metodo de instancia {self.nome}"

obj = MinhaClasse(nome="Exemplo")
print(obj.metodo_instancia())