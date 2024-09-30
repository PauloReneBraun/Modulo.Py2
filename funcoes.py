#Exemplo 
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n Chamando a função saudacao:")

# Funcao com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(5)
print("Resultado da funcao quadrado:", resultado_quadrado)

# Funcao com multiplos parametos 
def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

print("\n Chamando a função soma:")
numero1 = 25
numero2 = 30
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e numero %s é %s"% (numero1, numero2, resultado_soma))