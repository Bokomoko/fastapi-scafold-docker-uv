# Projeto Barebones Python Moderno com UV

Este projeto é um exemplo de scaffold (esqueleto) minimalista para aplicações Python modernas, utilizando apenas o [uv](https://github.com/astral-sh/uv) como ferramenta de desenvolvimento. O objetivo é simplificar o setup e a manutenção, eliminando a necessidade de ferramentas adicionais para gerenciamento de pacotes, dependências, testes, deploys e ambientes virtuais.

## Principais Características

- **Gerenciamento de dependências**: O `uv` substitui ferramentas como pip, pip-tools, poetry e pipenv, permitindo instalar, atualizar e remover dependências de forma rápida e eficiente.
- **Ambiente virtual automático**: O `uv` cria e gerencia ambientes virtuais automaticamente, sem necessidade de comandos extras.
- **Execução de scripts e testes**: Use o `uv` para rodar scripts, servidores de desenvolvimento e testes, sem precisar de `make`, `tox` ou `nox`.
- **Deploy simplificado**: O ambiente é reproduzível e fácil de portar para produção, já que o `uv` utiliza arquivos padrão como `pyproject.toml` e `requirements.txt`.

## Estrutura do Projeto

```txt
src/
  app.py
  project.toml
  hello_svc/
    __init__.py
    views.py
    entrypoints/
      __init__.py
      asgi.py
      cli.py
      queue_worker.py
  tests/
    test_e2e.py
```

- O código principal fica em `src/`.
- Entrypoints para diferentes modos de execução (ASGI, CLI, workers) ficam em `hello_svc/entrypoints/`.
- Testes ficam em `tests/`.

## Como Usar

1. **Instale o uv** (caso não tenha):

   ```sh
   curl -Ls https://astral.sh/uv/install.sh | sh
   # ou use Homebrew: brew install astral-sh/uv/uv
   ```

2. **Prepare o ambiente**:

   Instale o Python (se necessário) e ferramentas auxiliares usando o próprio uv. Exemplos de uso dos comandos com parâmetros formais:

   ```sh
   # Instala a versão recomendada do Python para o projeto (detectada automaticamente pelo uv)
   uv python install --auto

   # Ou especifique uma versão desejada
   uv python install 3.12

   # Instale ferramentas auxiliares (exemplo: pytest, ruff, etc)
   uv tools install pytest ruff
   ```

3. **Execute o app**:

   ```sh
   uv run src/app.py
   ```

4. **Rode os testes**:

   ```sh
   uv run pytest
   ```


5. **Adicione/remova dependências**:

   Para adicionar uma dependência:

   ```sh
   uv add <pacote>
   ```

   Para remover:

   ```sh
   uv remove <pacote>
   ```

## Vantagens

- Setup rápido e sem fricção
- Menos arquivos e ferramentas para manter
- Ambiente sempre isolado e reproduzível
- Compatível com padrões modernos do ecossistema Python

## Observações

- O `uv` ainda está em evolução, mas já é estável para uso em projetos modernos.
- Para deploy, basta garantir que as dependências estejam listadas em `pyproject.toml`.
- Ative as facilidades em preview exportando a variável de ambiente

```sh
export UV_PREVIEW=1`.
```

---

Este scaffold serve como ponto de partida para projetos Python enxutos, produtivos e fáceis de manter.
