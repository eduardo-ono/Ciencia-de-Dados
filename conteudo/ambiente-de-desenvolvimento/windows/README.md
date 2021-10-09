> Ciência de Dados > Conteúdo > Ambiente de Desenvolvimento

# Instalação do JupyterLab no Windows

Prof. Eduardo Ono

<br>

## Opção 1: Python

* Download

  * https://www.python.org/downloads/

* Instalação

  * Marcar a opção para incluir o Python no PATH.

    <img src="./img/python-install-path.png" alt="img" width="200">

<br>

## Opção 2: Anaconda

* Overview

  * Incluído no Anaconda:

    * Python (verificar a versão contida)
    * JupyterLab
    * Jupyter Notebook

* Download

  * https://www.anaconda.com/products/individual#Downloads

* Instalação

  * Instalar com as opções padrão excetuando a opção a seguir:

    <img src="./img/anaconda_install-path.png" alt="img" width="200">

<br>

## Opção 3: Miniconda + Pacotes

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
