> <h5>Ciência de Dados > Conteúdo > Python > Ambiente de Desenvolvimento</h5>

# Ambientes Virtuais

Prof. Eduardo Ono

<br>

## Overview

Alguns Sistemas Operacionais como o Linux/Ubuntu já trazem o Python instalado juntamente com o S.O. Nestes casos, é altamente recomendado que a versão não seja alterada, ou mesmo atualizada manualmente, visto que programas podem depender da versão instalada. Portanto, ambientes virtuais devem ser criados.

> O  ___Pip___ é um módulo do Python para gerenciamento de pacotes, necessários na constituição de ambientes virtuais.

> O ___venv___ é um gerenciador de ambientes virtuais para o Python.

<br>

## Instalação do Pip

### Windows

No ambiente Windows __não__ é necessária a instalação do Pip pois o mesmo está integrado na instalação "default" do Python 3.x.

### Linux/Ubuntu

Antes de instalar o Pip, verificar se o mesmo já não está instalado

```sh
pip --version
```

```sh
sudo apt update && sudo apt upgrade
sudo apt install python3-pip
```

### Atualizando o Pip

```sh
python -m pip install --upgrade pip
```

## Gerenciando Pacotes com o Pip

* Listar os pacotes instalados pelo Pip:

  ```sh
  pip list
  ```

* Instalar pacotes do Python:

  ```sh
  pip install <packages-name>
  ```

  * Exemplos

    Instala a versão mais recente do Numpy:

    ```sh
    pip install numpy
    ```

    Instala uma versão específica do Pandas:

    ```sh
    pip install pandas==1.1.0
    ```

* Salvar a lista dos pacotes instalados em um ambiente virtual

  ```sh
  pip freeze > requirements.txt
  ```

    * Exemplo de um arquivo `requirements.txt`:

      ```txt
      numpy==1.17.4
      pandas==0.25.3
      ```

* Recriar um ambiente virtual com seus pacotes especificados no arquivo `requirements.txt`

  ```sh
  pip install -r requirements.txt
  ```

* Exibir o(s) diretório(s) onde os pacotes podem ser instalados:

  ```python
  # Python
  import site
  site.getsitepackages()
  ```

<br>

## Gerenciando Ambientes Virtuais

* Documentação:

  * https://docs.python-guide.org/dev/virtualenvs/#virtualenvironments-ref

* Criar um ambiente virtual ("venv", de _virtual environment_):

  ```sh
  python -m venv <venv_name>
  ```

  * Exemplos:

    ```sh
    python -m venv abacaxi
    python -m venv venv-data-science
    ```

* Ativar um ambiente virtual

  ```sh
  source <env_name>/bin/activate
  ```

## Gerenciando Pacontes dentro de um Ambiente virtual

* Ativar um ambiente virtual
* Instalar os pacotes através do comando `pip install <packages-name>`

<br>

### Vídeos de Apoio

| Thumb | Descrição |
| :-: | --- |
|

* https://www.youtube.com/watch?v=z6_35nNKy0Y

<br>
