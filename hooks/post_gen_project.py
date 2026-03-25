import os
import shutil
import subprocess
import sys

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PYTHON_VERSION = "{{ cookiecutter.python_version }}"
REMOTE_URL = "{{ cookiecutter.git_remote_url }}"
CREATE_PIPELINE = "{{ cookiecutter.create_pipeline }}" == "True"
USE_GIT = "{{ cookiecutter.use_git }}" == "True"
INIT_UV = "{{ cookiecutter.init_uv }}" == "True"

RUFF_CONFIG = """

[tool.ruff]
line-length = 79

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']
ignore = ['E402', 'F811']
"""


def run_command(command, cwd=PROJECT_DIRECTORY, ignore_errors=False):
    try:
        subprocess.check_call(
            command,
            cwd=cwd,
            stdout=subprocess.DEVNULL if not ignore_errors else None,
            stderr=subprocess.DEVNULL if not ignore_errors else None,
        )
        return True
    except subprocess.CalledProcessError as e:
        if not ignore_errors:
            print(f"❌ Erro ao executar {' '.join(command)}: {e}")
        return False


def init_git_and_push():
    print("\n🐙 Inicializando Git...")

    if not run_command(["git", "init", "-b", "main"]):
        return

    run_command(["git", "add", "."])
    run_command(["git", "commit", "-m", "chore: initial commit from template"])
    print("✅ Git inicializado e commit realizado.")

    if REMOTE_URL and REMOTE_URL.strip():
        print(f"🚀 Configurando remote: {REMOTE_URL}")
        run_command(["git", "remote", "add", "origin", REMOTE_URL])
        run_command(["git", "branch", "-M", "main"])
        print("📤 Realizando push inicial...")
        if run_command(["git", "push", "-uf", "origin", "main"]):
            print("✅ Código enviado para o repositório remoto com sucesso!")
        else:
            print(
                "⚠️ Falha no push. Verifique se o repositório existe e se você tem permissão."
            )
    else:
        print("ℹ️ Nenhum remote configurado (URL vazia).")


def create_gitignore():
    gitignore_path = os.path.join(PROJECT_DIRECTORY, ".gitignore")
    content = """\
# Python
__pycache__/
*.py[cod]
.venv/
env/

# Config / Secrets
config/.env
.env

# Data
data/external/*
data/interim/*
data/processed/*
data/raw/*
!data/raw/.gitkeep

# Models (artefatos, binários)
models/*
!models/.gitkeep

# Jupyter
.ipynb_checkpoints
*/.ipynb_checkpoints/*

# IDE
.vscode/
.idea/
"""
    with open(gitignore_path, "w") as f:
        f.write(content)


def init_uv():
    print(f"\n📦 Inicializando UV (Python {PYTHON_VERSION})...")
    if run_command(["uv", "init", "--python", PYTHON_VERSION]):
        for f in ["hello.py", "main.py"]:
            p = os.path.join(PROJECT_DIRECTORY, f)
            if os.path.exists(p):
                os.remove(p)
    else:
        print("⚠️ uv não encontrado ou erro na inicialização.")
        return

    print("📦 Instalando ruff como dependência de desenvolvimento...")
    run_command(["uv", "add", "--dev", "ruff"])

    append_ruff_config()


def append_ruff_config():
    pyproject_path = os.path.join(PROJECT_DIRECTORY, "pyproject.toml")
    if not os.path.exists(pyproject_path):
        print("⚠️ pyproject.toml não encontrado, pulando configuração do ruff.")
        return

    with open(pyproject_path, "a") as f:
        f.write(RUFF_CONFIG)
    print("✅ Configuração do ruff adicionada ao pyproject.toml.")


def remove_pipeline():
    pipe_dir = os.path.join(PROJECT_DIRECTORY, "pipe")
    if os.path.exists(pipe_dir):
        shutil.rmtree(pipe_dir)
        print("🗑️ Diretório pipe/ removido (create_pipeline=False).")


if __name__ == "__main__":
    create_gitignore()

    if not CREATE_PIPELINE:
        remove_pipeline()

    if INIT_UV:
        init_uv()

    if USE_GIT:
        init_git_and_push()
