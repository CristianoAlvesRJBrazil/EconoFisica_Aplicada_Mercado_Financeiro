# Notebooks das aulas

Cada capítulo do livro-curso tem uma aula. O notebook da aula acompanha o capítulo, com as
listagens do livro, demonstrações para executar, uma prática guiada e os exercícios com
células para as respostas.

| Aula | Notebook | Duração |
|---|---|---|
| Caderno 0, Capítulo 1 — O ambiente de trabalho | [`aula_c0_cap01_ambiente_de_trabalho.ipynb`](caderno-0/aula_c0_cap01_ambiente_de_trabalho.ipynb) | 1h30 |
| Caderno 0, Capítulo 2 — Python essencial | [`aula_c0_cap02_python_essencial.ipynb`](caderno-0/aula_c0_cap02_python_essencial.ipynb) | 2h30 |
| Caderno 1, Capítulo 1 — O que é a Econofísica | [`aula_c1_cap01_o_que_e_a_econofisica.ipynb`](caderno-1/aula_c1_cap01_o_que_e_a_econofisica.ipynb) | 1h |
| Caderno 1, Capítulo 2 — De Bachelier a Mandelbrot | [`aula_c1_cap02_de_bachelier_a_mandelbrot.ipynb`](caderno-1/aula_c1_cap02_de_bachelier_a_mandelbrot.ipynb) | 1h |

## Como usar

1. Crie o ambiente do caderno, como explica o README do [Caderno 0](../caderno-0/) ou do
   [Caderno 1](../caderno-1/), e abra o JupyterLab (ou o VS Code) com ele ativado.
2. Abra o notebook da aula e execute as células **na ordem**, com `Shift+Enter`.
3. Ao terminar, reinicie o kernel, execute todas as células e confira se tudo roda do
   início ao fim.

Os notebooks são entregues sem saídas, para que cada um produza as suas. Depois de cada
célula, uma "Saída esperada" mostra o que deve aparecer.

Os exercícios de código têm, logo abaixo, uma célula de conferência. Ela responde *ok*,
*confira* (com uma pista) ou *ainda não resolvido*, sem interromper o notebook.

## Onde deixar os notebooks

Mantenha a estrutura de pastas do repositório. Os notebooks procuram os arquivos do
caderno a partir da própria pasta, subindo pelas pastas acima.

- **Caderno 0, Capítulo 1:** confere as bibliotecas instaladas contra o
  `requirements.txt` do Caderno 0. Cria as pastas `dados/` e `figuras/` ao lado do
  notebook.
- **Caderno 0, Capítulo 2:** usa só a biblioteca padrão do Python.
- **Caderno 1:** a primeira célula encontra a pasta `caderno-1/codigo/`, onde ficam o
  módulo de dados e a pasta `dados/`, e passa a trabalhar nela.
  - A aula do Capítulo 1 baixa as séries do S&P 500 e do Ibovespa na primeira execução.
    Por isso, faça-a antes da do Capítulo 2.
  - A aula do Capítulo 2 grava as figuras do livro em `caderno-1/codigo/figuras/`.

Se a busca falhar, por exemplo porque o notebook foi copiado para outro lugar, a mensagem
de erro diz o que fazer. Basta escrever o caminho na variável indicada no começo da
célula: `PASTA_CODIGO` nas aulas do Caderno 1, ou `REQUISITOS` na do Caderno 0.

Nada do que os notebooks gravam (dados baixados, figuras, pastas criadas) entra no
repositório: o `.gitignore` deixa esses arquivos de fora. Os dados de mercado devem ser
baixados por cada um e não devem ser redistribuídos.

Os slides citados no notebook do Caderno 0, Capítulo 1, acompanham o curso e não estão
neste repositório.
