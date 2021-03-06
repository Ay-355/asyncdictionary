from setuptools import setup
import re

# https://github.com/Rapptz/discord.py/blob/master/setup.py

requirements = []
with open("requirements.txt") as f:
    requirements = f.read().splitlines()


version = ""
with open("asyncdictionary/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)


readme = ""
with open("README.md") as f:
    readme = f.read()

setup(
    name="asyncdictionary",
    author="Ay355",
    license="MIT",
    url="https://github.com/Ay-355/asyncdictionary",
    version=version,
    packages=["asyncdictionary"],
    description="An asynchronous wrapper in python for the https://dictionaryapi.dev API",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    python_requires=">=3.6.0",
    keywords=[
        "dictionary",
        "api",
        "wrapper",
        "asyncdictionary",
        "async",
        "pythondictionary",
        "dictionary api",
        "asyncdictionary api",
    ],
    project_urls={
        "Documentation": "https://github.com/Ay-355/asyncdictionary/blob/master/Documentation.md",
        "Issue Tracker": "https://github.com/Ay-355/asyncdictionary/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
