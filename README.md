# Oversized

Profuder’s rebranded music label.

## Get Started

### Install Oversized

#### Prepare a Python Environment

To install Oversized and all its dependencies, Python needs to be installed on your system. Using a dedicated virtual
environment is highly recommended. For instance, with Anaconda:

```shell
conda create -n oversized python
conda activate oversized
```

#### Install the Development Version

You can install the development version from the sources. You first need to clone the project on your system. For
stability reasons, it is recommended to stay on the branch `master`, unless you want to try upcoming features or to
contribute to the project. You can then install the package from the sources:

```shell
pip install --extra-index-url "https://download.pytorch.org/whl/cu118" -e ".[dev]"
```

_Note: This command must be run in the project root directory._
