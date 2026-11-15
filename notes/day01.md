# Day 01: Workspace setup

1. A venv (`.venv`) is a private folder of packages for one project, like Laravel's `vendor/`, so two projects never fight over package versions.
2. `pip install rich` downloads a package into the active venv only, like `composer require`.
3. `pip freeze > requirements.txt` writes down every installed package with its exact version (rich plus its dependencies), like `composer.lock`.
4. `pip freeze` records what is installed; `pip install -r requirements.txt` does the reverse and rebuilds that same set on a fresh machine, which is why `.venv/` is git-ignored.
5. I ran Python 3.12 in Docker (`python:3.12-slim`), so `sys.prefix` showed `/app/.venv`, a Linux path inside the container, instead of a Windows path; a container isolates like a venv, but at the whole-OS level.
6. When you run python -m assistant.hello, Python sets __name__ to "__main__", so main() runs. When another file runs import assistant.hello, __name__ is "assistant.hello" instead, so main() doesn't run. The import just loads the functions without printing anything.