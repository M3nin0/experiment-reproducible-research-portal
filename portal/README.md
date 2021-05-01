### Portal

Este componente representa a biblioteca digital para a publicação de análises reprodutíveis.

**Execução automática**

Para fazer toda a configuração do portal, é possível utilizar os comandos registrados no `Makefile`. O primeiro passo é realizar a configuração do ambiente:

```shell
make environment
```

Agora, faça a instalação dos pacotes utilizados pelo portal

```shell
make invenio_packages
```

Inicie os serviços

```shell
make invenio_services
```

Por fim, inicialize o portal
```shell
make invenio_run
```

O comando abaixo realiza todos os passos descritos anteriormente

```shell
make portal
```

**Execução manual**

Se por algum motivo for necessário, é possível realizar os passos manualmente. Abaixo, são listados cada um deles

1° - Criação do ambiente virtual
```shell
python3 -m venv venv

source venv/bin/activate
```

2° - Instalação do `invenio-cli`
```shell
pip install invenio-cli wheel
```

3° - Configuração do `.invenio.private`

Nesta etapa será necessário criar um arquivo com o seguinte conteúdo

```
[cli]
project_dir = your-path/datacube-reproducible-service/portal/brazil-data-cube-reproducible-research
instance_path = your-path/datacube-reproducible-service/portal/venv/var/instance
services_setup = True

```

> **Note** que será necessário substituir o `your-path` dos *paths* para o equivalente em seu sistema de arquivos

4° - Instalação das dependências e geração da árvore de dependências
```shell
cd brazil-data-cube-reproducible-research

invenio-cli packages lock --pre --dev
invenio-cli install --pre --development
```

5° - Configuração dos serviços para a execução do portal
```shell
invenio-cli services setup --force
```

6° - Executando!
```shell
invenio-cli run
```

**Obtendo um token para a API Restful**

Para obter a *token* de acesso, pode-se utilizar a conta de um usuário admin. A criação deste usuário pode ser feita através do `invenio-cli`. Neste projeto, os comandos foram automatizados através do `make`. Assim, obtem-se a *token* através do seguinte comando:

```shell
make admin
```

Caso seja necessário a execução do passo a passo manual, consulte a [documentação do Invenio RDM](https://inveniordm.docs.cern.ch/customize/disabled/#test-that-super-users-are-allowed).
