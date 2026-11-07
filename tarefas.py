from armazenamento import salvar_tarefas


def adicionar_tarefa(tarefas, descricao):
    """Adiciona uma nova tarefa à lista e salva os dados."""
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)


def listar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas."""
    print("\n--- SUAS TAREFAS ---")

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f'{indice}. [{status}] {tarefa["descricao"]}')


def concluir_tarefa(tarefas, numero):
    """Marca uma tarefa como concluída. Retorna True se funcionar."""
    indice = numero - 1

    if 0 <= indice < len(tarefas):
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        return True

    return False


def excluir_tarefa(tarefas, numero):
    """Remove uma tarefa pelo número exibido no menu."""
    indice = numero - 1

    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        return True

    return False
