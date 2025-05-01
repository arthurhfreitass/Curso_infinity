def menu():
    print("~" * (len("Gerenciador de Tarefas ") + 4))
    print("  Gerenciador de Tarefas   ")
    print("~" * (len("Gerenciador de Tarefas ") + 4))
    print()
    print("1. Adicionar tarefas.")
    print("2. Concluir Tarefas")
    print("3. Ver todas as tarefas.")
    print("4. Excluir tarefas")
    print("5. Sair")


def add_tarefa(lista):
    nome = input("Nome da tarefa: ").capitalize()
    descricao = input("Descrição da tarefa: ").capitalize()
    prioridade = input("Prioridade (Alta, Média, Baixa): ").capitalize()
    categoria = input("Categoria (Ex: Estudo, Trabalho): ").capitalize()
    concluida = False

    lista.append({
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": concluida
        })
    
    print("Tarefa adicionada com sucesso!")


def mostrar_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(lista, start=1):
        status = "concluida" if tarefa["concluida"] else "não concluida"
        print(f"{i}- Nome: {tarefa["nome"]} | Descrição: {tarefa["descricao"]} | Prioridade: {tarefa["prioridade"]} | Categoria:{tarefa["categoria"]} | Status: {status}")


def concluir_tarefa(lista):
    if not lista:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(lista, start=1):
        status = "concluida" if tarefa["concluida"] else "não concluida"
        print(f"{i}- Nome: {tarefa["nome"]} | Descrição: {tarefa["descricao"]} | Prioridade: {tarefa["prioridade"]} | Categoria:{tarefa["categoria"]} | Status: {status}")

    print()
    opcao = int(input("Qual a tarefa que você deseja marca como concluida: "))

    if 0 <= (opcao - 1) < len(lista):
        lista[opcao - 1]["concluida"] = True
        print("Tarefa concluida com sucesso!")
    else:
        print("Tarefa não encontrada.")


def dell_tarefas(lista):
    if not lista:
        print("Nenhuma tarefa cadastrada.")
        return
    for i, tarefa in enumerate(lista, start=1):
        status = "concluida" if tarefa["concluida"] else "não concluida"
        print(f"{i}- Nome: {tarefa["nome"]} | Descrição: {tarefa["descricao"]} | Prioridade: {tarefa["prioridade"]} | Categoria:{tarefa["categoria"]} | Status: {status}")

    print()
    opcao = int(input("Qual a tarefa que você deseja excluir: "))

    if 0 <= (opcao - 1) < len(lista):
        removida = lista.pop(opcao -1)
        print(f"A tarefa '{removida}' foi removida com sucesso!")
    else:
        print("Tarefa não encontrada.")
    
lista = []
while True:
    menu()

    opcao = input("Selecione uma opção: ")

    if opcao == "5":
        print("Encerrando o programa...")
        break
    if opcao == "1":
        add_tarefa(lista)
    elif opcao == "2":
        concluir_tarefa(lista)
    elif opcao == "3":
        mostrar_tarefas(lista)
    elif opcao == "4":
        dell_tarefas(lista)
    else:
        print("Opção invalida.")


