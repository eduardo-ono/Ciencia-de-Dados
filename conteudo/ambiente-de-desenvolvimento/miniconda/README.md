> <h5>Ciência de Dados > Conteúdo > Ambiente de Desenvolvimento</h5>

# Miniconda

Prof. Eduardo Ono

<br>

## Tópicos

* ### Overview

* ### Instalação do Miniconda + Pacotes (Windows)

* Overview

  * Incluidos:

    * Python

      https://www.youtube.com/watch?v=XCvgyvBFjyM

* Download

  * https://docs.conda.io/en/latest/miniconda.html

* Instalação do Miniconda

  * Opções "default" exceto:

    <img src="./img/anaconda_install-path.png" alt="img" width="200">

* Instalação do JupyterLab

  ```cmd
  conda install -c conda-forge jupyterlab
  ```

  * Solução de possíveis erros na instalação do JupyterLab

    * Erro: "The Jupyter Server requires tornado"
    * Solução:

      ```cmd
      pip install --upgrade tornado
      ```

    * Erro: "ImportError: DLL load failed while importing win32api"
    * Possíveis soluções:

      ```cmd
      conda install pywin32
      ```

      ```cmd
      pip install --upgrade pywin32
      ```

      ```cmd
      pip install --upgrade jupyter_client
      ```

<br>

## Instalação e Configuração do Miniconda (Linux)

#### Criar um ambiente (abreviado aqui como "env", de _environment_)

```sh
conda create -n <env_name>
# ou
conda create --name <env_name>
```

* Exemplos

  ```sh
  conda create -n abacaxi
  conda create --name env_data-science
  ```

#### Criar um novo ambiente com alguns pacotes

```sh
conda create -n <env_name> pandas numpy matplotlib scikit-learn
```

#### Ativar um ambiente

Para que um ambiente virtual possa ser utilizado, o mesmo deve ser ativado:

```sh
conda activate <env_name>
```

#### Desativar o ambiente atual

```sh
conda deactivate
```

#### Desativar um ambiente

```sh
conda deactivate <env_name>
```

#### Desativar o ambiente (base)

```sh
conda config --set auto_activate_base false
```

#### Ativar o ambiente (base)

```sh
conda config --set auto_activate_base true
```

<br>

## Gerenciando Bibliotecas em um Ambiente

### Instalação de uma nova biblioteca

* Ativar um ambiente já previamente criado:

  ```sh
  conda activate <env_name>
  ```

* Instalar a biblioteca (_lib_)

  ```sh
  conda install <lib_name>
  ```

  * Exemplo

    ```sh
    conda install numpy
    ```

* Exportar a lista de pacotes de um ambiente para um arquivo

  ```sh
  conda env export > environment.yml
  ```

* Recriar um ambiente a partir do arquivo `environment.yml`

  ```sh
  conda env create -f environment.yml
  ```

<br>

## Instalação do Jupyter Lab (Linux/Ubuntu) através do Conda

* Ativar um ambiente

  ```sh
  conda activate <env_name>
  ```

* Instalar o Jupyter Lab

  ```sh
  conda install jupyterlab
  ```

  ou, caso prefira o repositório `conda-forge`:

  ```sh
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

| Thumb | Descrição |
| :-: | --- |
| [![img](https://img.youtube.com/vi/8laFJI2l3gU/default.jpg)](https://www.youtube.com/watch?v=8laFJI2l3gU) | <sup>[Ciência Programada]</sup> [__Criando um ambiente virtual para seu projeto Python__](https://www.youtube.com/watch?v=8laFJI2l3gU) <br> <sub>(1:18:40, YouTube, Ago/2020)</sub>

<br>
