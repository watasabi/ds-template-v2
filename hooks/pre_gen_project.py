"""
{{ cookiecutter.update({ "full_name": cookiecutter.full_name if cookiecutter.full_name != "Your Name" else get_git_user_name() }) }}
{{ cookiecutter.update({ "email": cookiecutter.email if cookiecutter.email != "Your Email" else get_git_user_email() }) }}
"""

import re
import sys



project_slug = "{{ cookiecutter.project_slug }}"
email = "{{ cookiecutter.email }}"
git_remote_url = "{{ cookiecutter.git_remote_url }}"

if hasattr(project_slug, "isidentifier"):
    if not project_slug.isidentifier():
        print(
            f"ERROR: O slug do projeto '{project_slug}' não é um nome válido de pacote Python."
        )
        sys.exit(1)
