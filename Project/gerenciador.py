def adicionar_tarefa(tarefas, nome_tarefa="tarefa padrão"):

  # TAREFA: NOME DA TAREFA
  # COMPLETADA: indica se a tarefa foi completada ou não

  tarefa = { "tarefa": nome_tarefa, "completada": False }

  tarefas.append(nome_tarefa)
  print(f"Tarefa {nome_tarefa} foi Adicionando ")
  return

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  if int(indice_tarefa) > len(tarefas):
    print("Tarefa não encontrada")
    return
  indice_tarefa_ajustado = int(indice_tarefa) - 1  
  if indice_tarefa_ajustado < 0 and indice_tarefa_ajustado >= len(tarefas):
    print("Tarefa não encontrada")
  tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
  print(f"Tarefa {indice_tarefa} foi atualizada para {novo_nome_tarefa}")
  return

def ver_tarefas(tarefas):
  print("\nTarefas:")
  for indice, tarefa in enumerate(tarefas):
    status = "✓" if tarefa["completada"] else ""
    print(f"{indice + 1}. {tarefa['tarefa']} - {'completada' if tarefa['completada'] else 'não completada'}")
  return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    if int(indice_tarefa) > len(tarefas):
      print("Tarefa não encontrada")
      return
   
def deletar_tarefas_completadas(tarefas):
  for tarefa in tarefas:
    if tarefa["completada"]:
      tarefas.remove(tarefa)
  print("Tarefas completadas foram deletadas")
  return

tarefas = []

while True:
  print("\nMenu do Gerenciador de tarefas:")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4 Completar tarefa")
  print("5. Deletar tarefa completas")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa: ")
    adicionar_tarefa(tarefas, nome_tarefa =nome_tarefa)
  elif escolha == "2":
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Digite o índice da tarefa que deseja atualizar: "))

  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = int(input("Digite o índice da tarefa que deseja completar: "))
    completar_tarefa(tarefas, indice_tarefa)

  elif escolha == "5":
    deletar_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)
    novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa)
  if escolha == "6":
    break

print("Programa Finalizado")