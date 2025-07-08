# Python Project Bootstrapper

A command-line tool to quickly scaffold new Python projects with popular frameworks and libraries. This bootstrapper creates a well-structured project directory with boilerplate code, configuration files, and optional features like Git initialization and virtual environments.

## Features

- **Multiple Templates**: Support for various Python frameworks and libraries
- **Interactive Mode**: User-friendly prompts for project setup
- **Git Integration**: Optional Git repository initialization
- **Virtual Environment**: Automatic virtual environment creation
- **License Support**: MIT and Apache license templates
- **Standard Structure**: Creates organized project directories with tests and documentation

## Supported Templates

| Template | Description | Dependencies |
|----------|-------------|--------------|
| `script` | Basic Python script (default) | None |
| `fastapi` | FastAPI web framework | fastapi, uvicorn |
| `flask` | Flask web framework | flask |
| `django` | Django web framework | django |
| `argparse` | Command-line tool with argparse | None |
| `click` | Command-line tool with Click | click |
| `selenium` | Web scraping/automation | selenium |
| `discordbot` | Discord bot template | discord.py |

## Installation

1. Save the script as `bootstrap.py` (or any name you prefer)
2. Make it executable: `chmod +x bootstrap.py`
3. Optionally, add it to your PATH for global access

## Usage

### Command Line Mode

```bash
# Basic usage
python bootstrap.py --name myproject

# With additional options
python bootstrap.py --name myproject --template fastapi --git-init --venv --license MIT --path ~/projects

# Full example
python bootstrap.py --name my-web-app --template flask --git-init --venv --license Apache --path ./projects
```

### Interactive Mode

```bash
python bootstrap.py --interactive
```

The interactive mode will prompt you for:
- Project name
- Git initialization (y/n)
- Virtual environment creation (y/n)
- License type (MIT/Apache/None)
- Output path (default: current directory)
- Template selection

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--name` | Name of the new project | Required (unless interactive) |
| `--path` | Directory to create the project in | Current directory |
| `--git-init` | Initialize Git repository | False |
| `--venv` | Create virtual environment | False |
| `--license` | Add LICENSE file (MIT/Apache) | None |
| `--template` | Choose project template | script |
| `--interactive` | Launch interactive mode | False |

## Project Structure

The bootstrapper creates the following directory structure:

```
myproject/
├── src/
│   ├── __init__.py
│   └── main.py          # Template-specific code
├── tests/
│   └── test_main.py     # Test file template
├── venv/                # Virtual environment (if --venv)
├── .git/                # Git repository (if --git-init)
├── .gitignore           # Python-specific gitignore
├── README.md            # Basic project README
├── requirements.txt     # Dependencies (if template has any)
└── LICENSE             # License file (if specified)
```

## Examples

### Create a FastAPI Project

```bash
python bootstrap.py --name my-api --template fastapi --git-init --venv --license MIT
```

This creates a FastAPI project with:
- FastAPI boilerplate code
- Git repository initialized
- Virtual environment created
- MIT license
- requirements.txt with fastapi and uvicorn

### Create a Discord Bot

```bash
python bootstrap.py --name discord-bot --template discordbot --venv --license Apache
```

### Interactive Flask Project

```bash
python bootstrap.py --interactive
# Then select flask template and configure options interactively
```

## Template Details

### FastAPI Template
- Creates a basic FastAPI app with a root endpoint
- Includes uvicorn for running the server
- Ready to run with: `uvicorn src.main:app --reload`

### Flask Template
- Basic Flask application with a home route
- Includes debug mode enabled
- Ready to run with: `python src/main.py`

### Django Template
- Placeholder with instructions for Django project creation
- Includes django in requirements.txt
- Use `django-admin startproject` for actual Django setup

### Discord Bot Template
- Basic bot with ping command
- Includes event handlers for bot ready state
- Requires Discord bot token configuration

## Getting Started After Creation

1. **Navigate to your project**:
   ```bash
   cd myproject
   ```

2. **Activate virtual environment** (if created):
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run your project**:
   ```bash
   python src/main.py
   ```

## License

This bootstrapper tool is created by Yeke Daniel and can be used to generate projects with MIT or Apache licenses.

## Contributing

Feel free to extend this tool by:
- Adding new templates
- Improving existing templates
- Adding more configuration options
- Enhancing the interactive mode

## Requirements

- Python 3.7+
- Git (optional, for --git-init)
- Internet connection (for installing dependencies)

---

*Happy coding! *