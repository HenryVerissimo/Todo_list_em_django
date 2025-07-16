### Fazer instalação do UV:

Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`

Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

### Instalar dependências do projeto:

`uv sync --all-groups`

Mais detalhes na <a href="https://docs.astral.sh/uv/getting-started/installation/">Documentação do UV</a>

### Ativar o ambiente no terminal (opcional):
Linux: `source .venv/bin/activate`

Windows: `.\.venv\Scripts\activate.ps1`

**ps:** Se o ambiente for ativado os comandos relacionados a dependências do projeto, podem ser feitos sem **"uv run"** no início do comando (**Ex:** uv run python3 main.py **-->** python3 main.py).

<hr>

### Comando para rodar o servidor:

`uv run python3 manage.py runserver` ou `task runserver`

**obs:** Alguns comandos personalizados foram adicionados ao projeto por meio da lib **<a href="https://pypi.org/project/taskipy/">Taskipy</a>** para facilitar ainda mais a sua vida. Todos os comandos estão listados em `[tool.taskipy.tasks]` no arquivo de configyrações `pyproject.toml`.

### Comando para criar migrações do banco:

`uv run python3 manage.py makemigrations` ou `task makemigrations`

### Comando para fazer migração de banco:

`uv run python3 manage.py migrate` ou `task migrate`

### Comandos para rodar o linter e format do ruff:

`uv run ruff format .` ou `task format`

`uv run ruff check .` ou `task lint`

**obs:** Esses dois comandos(lint e format) rodam automáticamente em todo commit graças aos hooks de pre-commit do projeto.