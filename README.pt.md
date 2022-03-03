Módulo para acessar o API da SpaceX
========================

(instructions in English: [README](https://github.com/thiagojcb/spacex_api/blob/main/README.md))

Este simples projeto acessa o [SpaceX API](https://docs.spacexdata.com/#bc65ba60-decf-4289-bb04-4ca9df01b9c1) para obter informações sobre o lançamento de seus foguetes.

O projeto também contém uma macro de seleção de dados, que compila algumas informações de interesse.

## Dependências
- Módulo:	`requests`, `pytest`
- Macro de seleção de dados: `pandas`, `openpyxl`

## Instalação

Uma vez que você clonou este repositório, em seu diretório principal o digite:

```BASH
$ make init
```

## Utilização

```PYTHON
from spacex_api import launches

# Devolve um tuple
got_launches, header = launches.get_launches()

# Imprime lista de lançamentos
print(got_launches)
```

## Macro de seleção de dados
Execute o seguinte comando:
```BASH
$ python launches_summary.py
```
A macro acima irá
- Indicar o ano que tem mais lançamentos
- Indicar o local onde aconteceu a maioria dos lançamentos
- Recuperar o número de lançamentos em um período específico de anos (ex: 2019, 2021)
- As informações acima são exportadas para um arquivo `.xlsx`

## Testando o módulo
O teste abaixo verificará se a API está sendo acessada com sucesso.
```BASH
$ make test
```

## Removendo o módulo
Para remover o módulo, digite:
```BASH
$ make remo
```

## Referências
- Este módulo é uma simplificação do [SpaceX-PY](https://github.com/hikaylum/spacex-py)
- A estrutura deste módulo é baseada no [Sample Module Repository](https://github.com/navdeep-G/samplemod)
