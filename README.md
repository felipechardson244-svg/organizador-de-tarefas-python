# Organizador de Tarefas em Python

Projeto de linha de comando desenvolvido para praticar fundamentos de Python e organização de código em módulos.

## Funcionalidades

- Adicionar tarefas.
- Listar tarefas cadastradas.
- Marcar tarefas como concluídas.
- Excluir tarefas.
- Salvar os dados automaticamente em um arquivo JSON, mantendo as tarefas após fechar o programa.

## Tecnologias e conceitos

- Python 3
- Listas e dicionários
- Funções
- Condicionais e laços de repetição
- Tratamento de exceções
- Manipulação de arquivos
- JSON
- Organização do projeto em módulos

## Como executar

1. Instale o Python 3.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

```bash
python main.py
```

No Windows, se o comando acima não funcionar, tente:

```bash
py main.py
```

## Organização dos arquivos

```text
organizador-de-tarefas/
├── main.py             # Menu e interação com o usuário
├── tarefas.py          # Funcionalidades de tarefas
├── armazenamento.py    # Leitura e gravação dos dados
├── dados/
│   └── tarefas.json    # Criado automaticamente ao salvar tarefas
├── README.md           # Documentação do projeto
└── .gitignore          # Arquivos que não devem ir para o Git
```

## Próximas melhorias sugeridas

- Adicionar prazo e prioridade às tarefas.
- Permitir editar a descrição.
- Criar testes automatizados com `unittest`.
- Desenvolver uma interface gráfica ou versão web.

## Autor

Felipe Chardson
