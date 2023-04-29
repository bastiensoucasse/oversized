"""
Package setup script for Oversized, Profuder’s rebranded music label.

To install the package and its dependencies, run:

    $ pip install .

This will download and install the package from the PyPI repository, along with its specified dependencies.

To install the package for development and testing, run:

    $ pip install -e ".[dev]"

This will install the package in editable mode, along with the development and testing dependencies.

For more information on how to use and contribute to the package, see the project repository at
https://github.com/bastiensoucasse/oversized.
"""

from typing import Dict

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

about: Dict[str, str] = {}
with open("oversized/__init__.py", encoding="utf-8") as f:
    exec(f.read(), about)

setup(
    name=about["__project__"],
    version=about["__version__"],
    description=about["__doc__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    maintainer=about["__maintainer__"],
    maintainer_email=about["__maintainer_email__"],
    packages=find_packages(),
    install_requires=[],
    extras_require={"dev": ["black", "mypy", "pylint", "pytest", "pytest-cov", "pytest-mypy"]},
)
