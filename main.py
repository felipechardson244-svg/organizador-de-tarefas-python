from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, excluir_tarefa
from armazenamento import carregar_tarefas


def mostrar_menu():
    print("\n=== ORGANIZADOR DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Concluir tarefa")
    print("4. Excluir tarefa")
    print("0. Sair")


def executar():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição da tarefa: ").strip()
            if descricao:
                adicionar_tarefa(tarefas, descricao)
                print("Tarefa adicionada com sucesso!")
            else:
                print("A descrição não pode ficar vazia.")

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            listar_tarefas(tarefas)
            try:
                numero = int(input("Número da tarefa concluída: "))
                if concluir_tarefa(tarefas, numero):
                    print("Tarefa marcada como concluída!")
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "4":
            listar_tarefas(tarefas)
            try:
                numero = int(input("Número da tarefa que deseja excluir: "))
                if excluir_tarefa(tarefas, numero):
                    print("Tarefa excluída!")
                else:
                    print("Número de tarefa inválido.")
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "0":
            print("Até mais! Suas tarefas foram salvas.")
            break

        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    executar()
