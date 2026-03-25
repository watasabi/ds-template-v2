import subprocess
from jinja2.ext import Extension


class LocalExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals.update(
            get_git_user_name=self.get_git_user_name,
            get_git_user_email=self.get_git_user_email,
        )

    def get_git_user_name(self):
        try:
            return (
                subprocess.check_output(
                    ["git", "config", "user.name"],
                    stderr=subprocess.DEVNULL,
                )
                .decode("utf-8")
                .strip()
                or "Your Name"
            )
        except Exception:
            return "Your Name"

    def get_git_user_email(self):
        try:
            return (
                subprocess.check_output(
                    ["git", "config", "user.email"],
                    stderr=subprocess.DEVNULL,
                )
                .decode("utf-8")
                .strip()
                or "email@example.com"
            )
        except Exception:
            return "email@example.com"
