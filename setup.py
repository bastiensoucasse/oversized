"""
Package setup script for Oversized, Profuder’s rebranded music label.

To install the package for development and testing, run:

    $ pip install -e ".[dev]"

This will install the package in editable mode, along with the development and testing dependencies.

For more information on how to use and contribute to the package, see the project repository at
https://github.com/bastiensoucasse/oversized.
"""

from typing import Dict, List

from setuptools import find_packages, setup  # type: ignore

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme: str = readme_file.read()

with open("requirements.txt", mode="r", encoding="utf-8") as requirements_file:
    requirements: List[str] = requirements_file.read().splitlines()

about: Dict[str, str] = {}
with open("oversized/__init__.py", mode="r", encoding="utf-8") as initialization_file:
    exec(initialization_file.read(), about)

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
    install_requires=requirements,
    extras_require={"dev": ["black", "mypy", "pylint"]},
)
