import argparse
import subprocess
from pathlib import Path


def create_project(name, git_init=False, use_venv=False, path=".", license_type=None, template="script"):
    project_path = Path(path) / name
    if not project_path.exists():
        project_path.mkdir()
        print(f"[+] Created project folder: {project_path}")

    src_path = project_path / "src"
    src_path.mkdir()
    (src_path / "__init__.py").touch()
    main_code = ""
    requirements = ""

    if template == "fastapi":
        main_code = '''from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    '''
        requirements = "fastapi\nuvicorn"

    elif template == "flask":
        main_code = '''from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        app.run(debug=True)
    '''
        requirements = "flask"

    elif template == "django":
        main_code = '''# Django projects are created using: django-admin startproject mysite
    # This is just a placeholder. Run this instead:
    # django-admin startproject mysite
    '''
        requirements = "django"

    elif template == "argparse":
        main_code = '''import argparse

    def main():
        parser = argparse.ArgumentParser(description="Your CLI tool description")
        parser.add_argument("--name", help="Your name")
        args = parser.parse_args()

        print(f"Hello, {args.name}!")

    if __name__ == "__main__":
        main()
    '''

    elif template == "click":
        main_code = '''import click

    @click.command()
    @click.option('--name', prompt='Your name', help='The person to greet.')
    def hello(name):
        click.echo(f"Hello, {name}!")

    if __name__ == "__main__":
        hello()
    '''
        requirements = "click"

    elif template == "selenium":
        main_code = '''from selenium import webdriver

    def main():
        driver = webdriver.Chrome()
        driver.get("https://example.com")
        print(driver.title)
        driver.quit()

    if __name__ == "__main__":
        main()
    '''
        requirements = "selenium"

    elif template == "discordbot":
        main_code = '''import discord
    from discord.ext import commands

    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f"Bot connected as {bot.user}")

    @bot.command()
    async def ping(ctx):
        await ctx.send("Pong!")

    if __name__ == "__main__":
        bot.run("YOUR_TOKEN_HERE")
    '''
        requirements = "discord.py"

    else:  # script
        main_code = '''def main():
        print("Hello from your new script!")

    if __name__ == "__main__":
        main()
    '''

    (src_path / "main.py").write_text(main_code)
    print(f"[+] Created main.py using {template} template")

    if requirements:
        (project_path / "requirements.txt").write_text(requirements)
        print("[+] Created requirements.txt")

    tests_path = project_path / "tests"
    tests_path.mkdir()
    (tests_path / "test_main.py").write_text("#Test cases go here\n")
    print("[+] Created tests/ directory and test_main.py")

    (project_path / "README.md").write_text(f"# {name.capitalize()}\n\nProject initialized with Python project Bootstrapper.\n")
    print("[+] Created README.md")

    gitignore_content = "__pycache__/\nvenv/\n.env\n*.pyc\n"
    (project_path / ".gitignore").write_text(gitignore_content)
    print("[+] Created .gitignore")

    if license_type:
        license_text =""
        if license_type.upper() == "MIT":
            license_text = "MIT License\n\nCopyright (c) 2025 Yeke Daniel"
        elif license_type.upper() == "Apache":
            license_text = "Apache License 2.0\n\nCopyright (c) 2025 Yeke Daniel"
        (project_path / "LICENSE").write_text(license_text)
        print(f"[+] Added {license_type.upper()} LICENSE")


    if git_init:
        subprocess.run(["git","init"], cwd=project_path)
        print("[+] Initialized empty git repository")

    if use_venv:
        subprocess.run(["python","-m", "venv","venv"], cwd=project_path)
        print("[+] Created virtual environment")

def run_interactive():
    print("Interactive Mode: Let's set up your Python project!\n")

    name = input("Project name: ").strip()
    git_init = input("Initialize Git? (y/n): ").lower().startswith("y")
    use_venv = input("Create virtual environment? (y/n): ").lower().startswith("y")
    license_type = input("License? (MIT/Apache/None): ").strip().capitalize()
    license_type = license_type if license_type in ["Mit", "Apache"] else None
    path = input("Output path (leave blank for current folder): ").strip() or "."
    template = input("Template? (script/fastapi/flask/django/argparse/click/selenium/discordbot): ").strip().lower()
    template = template if template in ["script", "fastapi", "flask", "django", "argparse", "click", "selenium","discordbot"] else "script"


    create_project(name, git_init, use_venv, path, license_type, template)


def main():
    parser = argparse.ArgumentParser(description="Python Project Bootstrapper")
    parser.add_argument("--name",help="Name of the new project")
    parser.add_argument("--path",default=".",help="Directory to create the project in")
    parser.add_argument("--git-init", action="store_true",help="Initialize Git repository")
    parser.add_argument("--venv",action="store_true",help="Create virtual environment")
    parser.add_argument("--license", choices=["MIT","Apache"], help="Add a LICENSE file")
    parser.add_argument("--interactive", action="store_true", help="Launch interactive mode")
    parser.add_argument("--template", choices=["script", "fastapi", "flask", "django", "argparse", "click", "selenium", "discordbot"], default="script", help="Choose a project template")



    args = parser.parse_args()

    if args.interactive:
        run_interactive()
    elif args.name:
        create_project(args.name, args.git_init, args.venv, args.path, args.license, args.template)

    else:
        print("Please provide a project name using --name or run in --interactive mode")

if __name__ == "__main__":
    main()
