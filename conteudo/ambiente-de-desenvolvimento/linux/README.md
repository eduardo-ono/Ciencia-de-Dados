> Ciência de Dados > Conteúdo > Ambiente de Desenvolvimento

# Linux (Unix)

Prof. Eduardo Ono

<br>

## Instalação do Python

<br>

## Instalação do Anaconda

```bash
sudo apt update && sudo apt upgrade
```

## Instalação do Miniconda


## Gerenciamneto de Ambientes com o Conda

* Criando um novo ambiente com os principais pacotes

```bash
conda create -n <nome_do_ambiente> pandas numpy matplotlib scikit-learn
```

* Ativando o ambiente

```bash
conda activate <nome_do_ambiente>
```

* Desativando o ambiente atual

```bash
conda deactivate <nome_do_ambiente>
```

* Deastivando o ambiente (base)

```bash
conda config --set auto_activate_base false
```

* Ativando o ambiente (base)

```
conda config --set auto_activate_base true
```

<br>

## Instalação do JupyterLab através do Conda

* Ativar um ambiente

```bash
conda activate <nome_do_ambiente>
```

* Instalar o JupyterLab

```bash
conda install jupyterlab
```

ou, caso prefira o repositório conda-forge

```bash
conda install -c conda-forge jupyterlab
```

Para executar o JupyterLab:

```
jupyter lab
```

<br>

## Links

* https://nbviewer.jupyter.org/
* https://nbviewer.jupyter.org/github/bokeh/bokeh-notebooks/blob/main/tutorial/06%20-%20Linking%20and%20Interactions.ipynb
* https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks
* https://github.com/rasbt/algorithms_in_ipython_notebooks
* https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
* https://www.dataschool.io/cloud-services-for-jupyter-notebook/

<br>
