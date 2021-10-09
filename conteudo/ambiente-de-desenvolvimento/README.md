> ### Ciência de Dados > Conteúdo

# Ambiente de Desenvolvimento

Prof. Eduardo Ono

<br>

* ## Sumário

* ### Instalação no Windows

  * Python
  * Python + Anaconda
  * Python + Miniconda + Pacotes

* ### Instalação no Linux (Ubuntu)

  * Python
  * Python + Anaconda
  * Python + Miniconda + Pacotes

<br>

## Instalação e Configuração do Miniconda (Linux)

* Criando um novo ambiente com os principais pacotes

  ```
  conda create -n nome_do_ambiente pandas numpy matplotlib scikit-learn
  ```

  ou

* Criando um novo ambiente com os principais pacotes

  ```
  conda create -n nome_do_ambiente pandas numpy matplotlib scikit-learn
  ```

* Ativando o ambiente

  ```
  conda activate nome_do_ambiente
  ```

* Desativando o ambiente atual

  ```
  conda deactivate nome_do_ambiente
  ```

* Deastivando o ambiente (base)

  ```
  conda config --set auto_activate_base false
  ```

* Ativando o ambiente (base)

  ```
  conda config --set auto_activate_base true
  ```

<br>

## Instalação do Jupyter Lab (Linux) através do Conda

* Ativar um ambiente

  ```
  conda activate nome_do_ambiente
  ```

* Instalar o Jupyter Lab

  ```
  conda install jupyterlab
  ```

  ou, caso prefira o repositório conda-forge

  ```
  conda install -c conda-forge jupyterlab
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
