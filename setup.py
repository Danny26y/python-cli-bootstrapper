from setuptools import setup, find_packages

setup(
    name="project-bootstrapper",
    version="0.1.0",
    packages=find_packages(),  # automatically finds the 'bootstrapper' package
    entry_points={
        "console_scripts": [
            "bootstrapper=bootstrapper.cli:main",  # 'main' function in cli.py
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to bootstrap Python projects with Git and venv support.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/project-bootstrapper",  # update this after pushing to GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
