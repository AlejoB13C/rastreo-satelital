# Proyecto Rastreo Satelital Team 56 guide installation

> You can set this runing the auto-install.py script (python3 auto-install.py)

## Prerequisites

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- \(Optional but required for auto-setup.py\) [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
conda activate ./env
```

or 

```bash
mamba env create -f environment.yml
conda activate ./env
```

The packages necessary to run the project are now installed inside the conda environment.

**Note: The following sections assume you are located in your conda environment.**  

## Set up project's module


To move beyond notebook prototyping, all reusable code should go into the `proyecto_rastreo_satelital_team_56/` folder package. To use that package inside your project, install the project's module in editable mode, so you can edit files in the `proyecto_rastreo_satelital_team_56` folder and use the modules inside your notebooks :

```bash
pip install --editable .
```
> this is automatically installed when create the environment

To use the module inside your notebooks, add `%autoreload` at the top of your notebook :

```python
%load_ext autoreload
%autoreload 2
```

Example of module usage :

```python
from proyecto_rastreo_satelital_team_56.utils.paths import data_dir
data_dir()
```

## Set up Git diff for notebooks and lab

We use [nbdime](https://nbdime.readthedocs.io/en/stable/index.html) for diffing and merging Jupyter notebooks.

To configure it to this git project :

```bash
nbdime config-git --enable
```

To enable notebook extension :

```bash
nbdime extensions --enable --sys-prefix
```

Or, if you prefer full control, you can run the individual steps:

```bash
jupyter serverextension enable --py nbdime --sys-prefix

jupyter nbextension install --py nbdime --sys-prefix
jupyter nbextension enable --py nbdime --sys-prefix

jupyter labextension install nbdime-jupyterlab
```

You may need to rebuild the extension : `jupyter lab build`  

