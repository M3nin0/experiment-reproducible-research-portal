### Portal

Este componente representa a biblioteca digital para a publicação de análises reprodutíveis.

**Executando**

1° - Criação do ambiente virtual
```shell
python3 -m venv venv

source venv/bin/activate
```

2° - Instalação do `invenio-cli`
```shell
pip install invenio-cli
```

3° - Instalação das dependências e geração da árvore de dependências
```shell
invenio-cli packages lock --pre --dev
invenio-cli install --pre --development
```

4° - Configuração dos serviços para a execução do portal
```shell
invenio-cli services setup
```

5° - Executando!
```shell
invenio-cli run
```
