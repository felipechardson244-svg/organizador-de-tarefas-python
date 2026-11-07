import json
from pathlib import Path

ARQUIVO_DADOS = Path(__file__).parent / "dados" / "tarefas.json"


def carregar_tarefas():
    """Carrega as tarefas do arquivo JSON. Se não existir, retorna lista vazia."""
    ARQUIVO_DADOS.parent.mkdir(exist_ok=True)

    if not ARQUIVO_DADOS.exists():
        return []

    try:
        with ARQUIVO_DADOS.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, OSError):
        print("Aviso: não foi possível ler os dados. Uma lista vazia será iniciada.")
        return []


def salvar_tarefas(tarefas):
    """Salva a lista de tarefas em formato JSON."""
    ARQUIVO_DADOS.parent.mkdir(exist_ok=True)

    with ARQUIVO_DADOS.open("w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)
