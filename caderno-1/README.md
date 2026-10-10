# Caderno 1 — Fundamentos da Econofísica: código

Código de todas as listagens do Caderno 1 do livro *Econofísica Aplicada ao Mercado
Financeiro*. A amostra em PDF está em [`../amostra/`](../amostra/).

## Organização

```
codigo/
├── requirements.txt       # versões fixadas (Python 3.12 ou superior), com statsmodels
├── matplotlibrc           # estilo de todas as figuras
├── dados_caderno1.py      # módulo de dados, importado por todos os capítulos
├── executar_listagens.py  # executa todas as listagens, em ordem
├── cap01/ ... cap05/      # um arquivo por listagem do livro
├── dados/                 # preenchida pela listagem que baixa os dados
└── figuras/               # preenchida pelas listagens que fazem gráficos
```

Cada arquivo `lCC_NN_*.py` é uma listagem do capítulo CC, na ordem em que aparece no
livro. O arquivo `cap01/l01_01_rede.py` baixa os dados; os demais só leem as cópias
locais.

## Como executar

```bash
cd caderno-1/codigo
python3.12 -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
python executar_listagens.py       # grava as saídas em ../saidas
```

Rode sempre a partir desta pasta (`codigo/`), porque os caminhos são relativos a ela. O
Caderno 1 não depende dos dados do Caderno 0: baixa as próprias séries.

## Dados

Os dados não estão no repositório. A primeira listagem baixa do Yahoo Finance o S&P 500
(de 1950 a 2025) e o Ibovespa (de 2000 a 2025) e grava cópias datadas em `dados/`.
Respeite os termos de uso da fonte e não redistribua os arquivos baixados.
