# Caderno 0 — Python para finanças quantitativas: código

Código de todas as listagens do Caderno 0 do livro *Econofísica Aplicada ao Mercado
Financeiro*. A amostra em PDF está em [`../amostra/`](../amostra/).

## Organização

```
codigo/
├── requirements.txt       # versões fixadas (Python 3.12 ou superior)
├── matplotlibrc           # estilo de todas as figuras
├── executar_listagens.py  # executa todas as listagens, em ordem
├── cap01/ ... cap06/      # um arquivo por listagem do livro
├── dados/                 # preenchida pelas listagens que baixam dados
└── figuras/               # preenchida pelas listagens que fazem gráficos
```

Cada arquivo `lCC_NN_*.py` é uma listagem do capítulo CC, na ordem em que aparece no
livro. Os arquivos `*_rede.py` baixam dados da internet. Os arquivos `*_erro.py` terminam
com um erro de propósito, para mostrar uma exceção. Os arquivos `t*` contêm comandos de
terminal.

## Como executar

```bash
cd caderno-0/codigo
python3.12 -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
python executar_listagens.py       # grava as saídas em ../saidas
```

Também dá para abrir as listagens no JupyterLab e executá-las em ordem, como células de
um notebook: as de um mesmo capítulo usam o que as anteriores criaram. Rode sempre a
partir desta pasta (`codigo/`), porque os caminhos são relativos a ela.

## Dados

Os dados não estão no repositório. As listagens `*_rede.py` baixam:

- os fechamentos de 2016 a 2025 do Yahoo Finance;
- o dólar do Banco Central (SGS, série 1);
- o arquivo anual de séries históricas da B3 de 2025, com cerca de 89 MB.

As cópias ficam em `dados/`, com a data do download no nome. Respeite os termos de uso de
cada fonte e não redistribua os arquivos baixados.

Os preços ajustados do Yahoo mudam a cada novo dividendo. Por isso, se você baixar os
dados em outra data, alguns números podem diferir ligeiramente dos impressos no livro. O
Capítulo 6 explica esse efeito.
