# Caderno 2 — Distribuições de cauda pesada: código

Código de todas as listagens do Caderno 2 do livro *Econofísica Aplicada ao Mercado
Financeiro*. O caderno trata das caudas pesadas dos retornos em cinco capítulos:

1. Momentos, curtose e caudas
2. Distribuições estáveis de Lévy (inclui a Lévy truncada)
3. A *t* de Student e outras alternativas
4. A lei cúbica inversa e o estimador de Hill
5. Agregação temporal

O PDF deste caderno ainda não está na amostra em [`../amostra/`](../amostra/), que traz os
Cadernos 0 e 1.

## Organização

```
codigo/
├── requirements.txt       # as mesmas versões do Caderno 1 (Python 3.12 ou superior)
├── matplotlibrc           # estilo de todas as figuras
├── dados_caderno2.py      # módulo de dados, importado por todos os capítulos
├── executar_listagens.py  # executa todas as listagens, em ordem
├── cap01/ ... cap05/      # um arquivo por listagem do livro (28 listagens)
├── dados/                 # preenchida pela listagem que baixa os dados
└── figuras/               # preenchida pelas listagens que fazem gráficos (8 figuras)
```

Cada arquivo `lCC_NN_*.py` é uma listagem do capítulo CC, na ordem em que aparece no
livro. O arquivo `cap01/l01_01_rede.py` baixa os dados; os demais só leem as cópias
locais.

## Como executar

```bash
cd caderno-2/codigo
python3.12 -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
python executar_listagens.py       # grava as saídas em ../saidas
```

O ambiente do Caderno 1 serve sem mudanças. Rode sempre a partir desta pasta (`codigo/`),
porque os caminhos são relativos a ela. Algumas listagens levam alguns segundos: as que
ajustam a distribuição NIG, simulam somas de distribuições estáveis e fazem os
*bootstraps*.

## Dados

Os dados não estão no repositório. A primeira listagem baixa do Yahoo Finance três
arquivos e grava cópias datadas em `dados/`:

- **Índices:** S&P 500 (desde 1950), Ibovespa (desde 2000), DAX (desde 1988) e Nikkei
  (desde 1965).
- **Ações brasileiras:** PETR4, VALE3, ITUB4, BBAS3 e SBSP3, de 2000 a 2025, com o
  Ibovespa.
- **Ações norte-americanas:** AAPL, MSFT, JPM, XOM e KO, de 2000 a 2025, com o S&P 500.

O índice de cada mercado serve de calendário: o módulo de dados só usa os dias em que ele
foi negociado, o que elimina as cotações que o Yahoo às vezes traz em feriados.

Antes de medir as caudas, os maiores movimentos das ações foram conferidos. Os das ações
brasileiras conferem com o arquivo oficial de cotações da B3. Um único dia é excluído,
com o motivo registrado no dicionário `EXCLUSOES` do módulo: o ITUB4 em 04/10/2021,
primeiro pregão sem o direito aos BDRs da XP (cisão). A queda de 18% desse dia não foi um
movimento de mercado.

Respeite os termos de uso da fonte e não redistribua os arquivos baixados.

## Alguns resultados

- Nas 14 séries, o expoente de cauda estimado pelo método de Hill tem média de 3,09 nas
  quedas e 3,12 nas altas: é a lei cúbica inversa.
- Pelo AIC, a distribuição NIG ajusta melhor o S&P 500 como um todo. Nas caudas, porém,
  só a *t* de Student acompanha os dados até 10 desvios-padrão.
- Somando os retornos em horizontes de até 20 pregões, o expoente das ações fica perto de
  3. Com os dias embaralhados, sobe para 5,1: é a dependência entre os dias que mantém as
  caudas pesadas.
