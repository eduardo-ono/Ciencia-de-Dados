
# Instalação do Miniconda no Linux

__Prof. Eduardo Ono__

&nbsp;

## Download

* https://docs.conda.io/en/latest/miniconda.html

* Download através do terminal:

```sh
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

&nbsp;

## Processo de Instalação

* Atualizar o Linux

```sh
sudo apt update && sudo apt upgrade
```

* Tornar executável o script de execução

```sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
```

* Instalar o Miniconda

```sh
./Miniconda3-latest-Linux-x86_64.sh
```

* Verificar a versão instalada do Conda

```sh
conda --v
```

* Atualizar o Conda

```sh
conda update conda
```

* Caso queira, desativar o ambiente base do Conda ao inicializar o terminal

```sh
conda config --set auto_activate_base false
```
