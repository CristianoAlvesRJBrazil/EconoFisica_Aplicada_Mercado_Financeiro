# Econofísica Aplicada ao Mercado Financeiro

**Física estatística, sistemas complexos e Python aplicados a dados de mercado**

Este repositório reúne o desenvolvimento de modelos e ferramentas de Econofísica: a área
que aplica teorias, conceitos e métodos estatísticos da física (como a mecânica
estatística, a dinâmica caótica e os fenômenos críticos) para modelar, analisar e
compreender o mercado financeiro como um sistema complexo.

O material é organizado como um livro-curso em **cadernos modulares**, um para cada
módulo de um curso de 84 horas. Cada caderno combina teoria concisa, código Python
executado com dados reais e exercícios em três níveis.

## Amostra: Cadernos 0 e 1

📘 **[Baixar a amostra em PDF](amostra/Econofisica_Aplicada_Mercado_Financeiro_Cadernos_0_e_1.pdf)**
(99 páginas, edição em construção, versão 0.1 de 10/10/2026)

### Caderno 0 — Python para finanças quantitativas (12 h)

1. O ambiente de trabalho
2. Python essencial
3. NumPy: cálculo vetorizado
4. pandas: séries temporais financeiras
5. Gráficos e estatística
6. Dados de mercado e retornos

### Caderno 1 — Fundamentos da Econofísica (6 h)

1. O que é a Econofísica
2. De Bachelier a Mandelbrot
3. Mercados eficientes e passeio aleatório
4. O modelo gaussiano e os fatos estilizados
5. Críticas e diálogo com a econometria

### Alguns resultados da amostra

Todos foram obtidos com o código do próprio livro:

- Entre 2016 e 2025, o Ibovespa teve quedas de mais de 5% num único dia com frequência
  cerca de 14 vezes maior do que a prevista pela distribuição normal.
- A queda do S&P 500 em 19/10/1987 equivale a 29 desvios-padrão da história do índice até
  a véspera. Pela normal, a probabilidade desse evento seria da ordem de 10⁻¹⁸⁷.
- Os retornos diários quase não têm autocorrelação, mas os retornos absolutos têm uma
  autocorrelação que persiste por meses: é o agrupamento de volatilidade.

## Código dos cadernos

Todo o código das listagens do livro está no repositório, com as versões fixadas usadas
para gerar a amostra:

- [`caderno-0/codigo/`](caderno-0/): Python, NumPy, pandas, gráficos, estatística e a
  base de dados de mercado (B3, Banco Central e Yahoo Finance). São 54 listagens.
- [`caderno-1/codigo/`](caderno-1/): passeio aleatório, mercados eficientes,
  autocorrelação, razão de variâncias, fatos estilizados e o modelo ARCH. São 22
  listagens.

Para executar um caderno:

```bash
cd caderno-1/codigo
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python executar_listagens.py
```

O README de cada caderno traz os detalhes.

## Plano do livro

| Caderno | Título | Horas | Situação |
|---|---|---|---|
| 0 | Python para finanças quantitativas | 12 | **na amostra** |
| 1 | Fundamentos da Econofísica | 6 | **na amostra** |
| 2 | Distribuições de cauda pesada | 8 | em preparação |
| 3 | Processos estocásticos em finanças | 8 | em preparação |
| 4 | Leis de potência e invariância de escala | 6 | em preparação |
| 5 | Fractais, memória longa e multifractalidade | 8 | em preparação |
| 6 | Correlações, matrizes aleatórias e redes | 8 | em preparação |
| 7 | Entropia e informação em séries temporais | 6 | em preparação |
| 8 | Modelos baseados em agentes | 8 | em preparação |
| 9 | Crises, bolhas e eventos extremos | 6 | em preparação |
| 10 | Projeto integrador | 8 | em preparação |

## Ferramentas e dados

- **Python 3.12**, com NumPy, pandas, SciPy, Matplotlib e statsmodels em versões fixadas.
- **Dados públicos de mercado:** B3 (séries históricas oficiais), Banco Central do Brasil
  (SGS) e Yahoo Finance (pela biblioteca `yfinance`).

Os dados não acompanham o repositório. O livro mostra como cada leitor baixa a própria
cópia, respeitando os termos de uso de cada fonte.

## Aviso

Material com finalidade exclusivamente educacional. Nenhum conteúdo, exemplo ou resultado
constitui recomendação de investimento. Resultados passados não garantem resultados
futuros.

## Autor

**Cristiano Alves** — © 2026. Edição em desenvolvimento: erros e sugestões são bem-vindos
pelas *issues* deste repositório.
