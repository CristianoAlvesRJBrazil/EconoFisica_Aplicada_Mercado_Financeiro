# Notebooks das aulas

Cada capítulo do livro-curso tem uma aula. O notebook da aula acompanha o capítulo, com as
listagens do livro, demonstrações para executar, uma prática guiada e os exercícios com
células para as respostas.

| Aula | Notebook | Duração |
|---|---|---|
| Caderno 0, Capítulo 1 — O ambiente de trabalho | [`aula_c0_cap01_ambiente_de_trabalho.ipynb`](caderno-0/aula_c0_cap01_ambiente_de_trabalho.ipynb) | 1h30 |
| Caderno 0, Capítulo 2 — Python essencial | [`aula_c0_cap02_python_essencial.ipynb`](caderno-0/aula_c0_cap02_python_essencial.ipynb) | 2h30 |

## Como usar

1. Crie o ambiente do Caderno 0, como explica o [README do caderno](../caderno-0/), e
   abra o JupyterLab com ele ativado.
2. Abra o notebook da aula e execute as células **na ordem**, com `Shift+Enter`.
3. Ao terminar, use *Kernel → Restart Kernel and Run All Cells* e confira se tudo roda do
   início ao fim.

Os notebooks são entregues sem saídas, para que cada um produza as suas. Depois de cada
célula, uma "Saída esperada" mostra o que deve aparecer.

O notebook do Capítulo 1 confere as bibliotecas instaladas contra o `requirements.txt` do
Caderno 0 e funciona aberto desta pasta. Se você copiá-lo para outra pasta, coloque-o ao lado
de um `requirements.txt`.

O do Capítulo 2 usa só a biblioteca padrão do Python. A célula de conferência de cada
exercício responde *ok*, *confira* (com uma pista) ou *ainda não resolvido*, sem interromper
o notebook.

Algumas células criam as pastas `dados/` e `figuras/` ao lado do notebook. O que for gravado
nelas não entra no repositório.

Os slides citados no notebook do Capítulo 1 acompanham o curso e não estão neste
repositório.
