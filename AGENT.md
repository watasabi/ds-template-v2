# Agent Guidelines for ds-template-v2

This document provides guidelines for AI agents working on this codebase. **Always keep these rules updated** as the project evolves.

## Project Overview

ds-template-v1 is a cookiecutter-based template for Data Scientists on the team.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Template Engine | Cookiecutter |
| Environment | UV + Python venv |
| Testing | pytest |
| Linting | Ruff |

## Project Structure

```
ds-template-v2/
├── cookiecutter.json           # Template variables and defaults
├── local_extensions.py         # Jinja2 extensions (git user info)
├── hooks/
│   ├── pre_gen_project.py      # Validation before generation
│   └── post_gen_project.py     # Setup after generation (uv, ruff, git)
├── {{cookiecutter.project_slug}}/
│   ├── README.md               # Project readme (templatized)
│   ├── AGENT.md                # AI agent guidelines (templatized)
│   ├── .cursorrules            # Cursor AI rules (templatized)
│   ├── .gitignore              # Git ignore rules
│   └── LICENSE                 # MIT License
├── AGENT.md                    # This file
├── .cursorrules                # Cursor rules for this template repo
└── README.md                   # Template documentation
```

## Code Conventions

- Python 3.12+ features (type hints, `|` union, etc.)
- Line length: 79 characters
- Use `ruff` for linting and formatting

```toml
[tool.ruff]
line-length = 79

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']
ignore = ['E402', 'F811']
```

- Docstrings for public APIs (Google style)
- **Always use type hints.**

## Commands

```bash
uv run ruff check src/ tests/           # Lint code
uv run ruff format src/ tests/          # Format code
```

## Important Rules

1. **Cookiecutter variables** use `{{ cookiecutter.variable }}` syntax inside `{{cookiecutter.project_slug}}/`.
2. **Hooks** run Python scripts — `pre_gen` validates, `post_gen` sets up the environment.
3. **local_extensions.py** provides `get_git_user_name()` and `get_git_user_email()` to Jinja2.
4. **Always add type hints** to function signatures.
