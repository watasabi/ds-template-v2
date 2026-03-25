# ds-template-v2

Template cookiecutter para projetos de Data Science.

## Funcionalidades

- Estrutura padronizada para projetos de DS
- Configuração automática com **UV** + **Ruff**
- Arquivos `.cursorrules` e `AGENT.md` para integração com Cursor AI
- Inicialização de Git com commit inicial
- Push automático para remote (opcional)
- Nome e email do autor extraídos automaticamente do Git config

## Pré-requisitos

### Instalar UV

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Após instalar, reinicie o terminal ou rode:

```bash
source $HOME/.local/bin/env
```

Para verificar a instalação:

```bash
uv --version
```

## Getting Started

```bash
uvx cookiecutter https://github.com/watasabi/ds-template-v2.git --checkout master
```

## Variáveis do Template

| Variável | Descrição | Default |
|----------|-----------|---------|
| `project_name` | Nome do projeto | `Project Name` |
| `project_slug` | Slug (auto-gerado) | baseado no `project_name` |
| `project_desc` | Descrição curta | `A short description of the project.` |
| `python_version` | Versão do Python | `3.14` |
| `full_name` | Nome do autor | extraído do `git config` |
| `email` | Email do autor | extraído do `git config` |
| `git_remote_url` | URL do repositório remoto | vazio |
| `create_pipeline` | Criar diretório `pipe/` | `true` |
| `use_git` | Inicializar Git | `true` |
| `init_uv` | Inicializar UV + instalar ruff | `true` |

## Project Organization

```
.
├── config/                 # Configurações e variáveis de ambiente
│   ├── .env                # Variáveis de ambiente (NÃO commitar!)
│   └── .env.example        # Template com as variáveis necessárias
│
├── data/                   # Dados do projeto (Geralmente ignorados pelo Git)
│   ├── external/           # Dados de fontes terceiras
│   ├── interim/            # Dados transformados intermediários
│   ├── processed/          # Dados finais prontos para modelagem
│   └── raw/                # Dados originais imutáveis
│
├── notebooks/              # Jupyter Notebooks
│   ├── eda/                # Análise exploratória de dados
│   ├── get_data/           # Extração de dados (usa queries/)
│   ├── processing/         # Transformação e feature engineering
│   ├── training/           # Treinamento de modelos
│   ├── modeling/           # Experimentos e avaliação de modelos
│   └── qa/                 # Validação e quality assurance
│
├── queries/                # Queries SQL (.sql) para Databricks
│   └── get_data/           # Queries usadas por notebooks/get_data/
│
├── pipe/                   # Orquestração e Pipeline de Produção
│   ├── orchestrator.py     # Orquestrador (ex: Azure ML, Airflow)
│   ├── src/                # Steps do pipeline (Scripts numerados)
│   │   ├── 01_load.py
│   │   ├── 02_preprocess.py
│   │   ├── 03_inference.py
│   │   └── 04_postprocess.py
│   └── utils/              # Utilitários específicos do pipeline
│
├── models/                 # Artefatos de modelos / UV sub-projects
│
├── reports/                # Relatórios gerados, html, pdf
│   └── figures/            # Gráficos e imagens geradas pelos códigos
│
├── src/                    # Código Fonte Reutilizável (Library do projeto)
│   └── __init__.py         # Funções de engenharia de features
│
├── .cursorrules            # Regras para o Cursor AI
├── AGENT.md                # Guidelines para agentes AI
├── .gitignore              # Arquivos a serem ignorados pelo git
├── LICENSE                 # Licença do projeto
├── pyproject.toml          # Dependências e config (UV workspace)
└── README.md               # Documentação principal
```
