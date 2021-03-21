## Data Cube Reproducible Service

Este serviço é um experimento que busca apresentar o fluxo de análise, processamento e publicação através de uma abordagem reprodutível.

### Portal

```shell
python3 -m venv venv

source venv/bin/activate
```

```shell
pip install invenio-cli
```

```shell
invenio-cli packages lock --pre --dev
invenio-cli install --pre --development
```

```shell
invenio-cli services setup
```

```shell
invenio-cli run
```
