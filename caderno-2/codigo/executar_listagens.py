"""Executa as listagens do Caderno 2 e grava as saídas que aparecem no livro.

As listagens de cada capítulo rodam em sequência, num mesmo espaço de nomes, como as
células de um notebook. A saída de cada uma vai para ../saidas/capNN/<listagem>.txt,
e o LaTeX inclui esses arquivos diretamente: o que está no livro é o que rodou.

Convenções de nome:
  *_rede.py  baixa dados da internet. Só roda se a saída ainda não existir ou se o
             script for chamado com --atualizar (os dados ficam em cópias datadas).
  *_erro.py  termina com um erro de propósito; grava a última linha da mensagem.

Uso, a partir desta pasta:  python executar_listagens.py [--atualizar] [cap02 ...]
"""
import contextlib
import io
import sys
import traceback
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # gera as figuras sem abrir janelas
import matplotlib.pyplot as plt
import pandas as pd

PASTA = Path(__file__).resolve().parent
SAIDAS = PASTA.parent / "saidas"

# Caracteres fora do ASCII que o estilo de listagem do livro sabe imprimir.
PERMITIDOS = set("áéíóúÁÉÍÓÚàâêôãõÂÊÔÃÕçÇüºª")

# Formato das tabelas impressas pelo pandas, para caber na largura da página.
pd.set_option("display.width", 82)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 4)


def caracteres_invalidos(texto):
    return sorted({c for c in texto if ord(c) > 127 and c not in PERMITIDOS})


def executar_capitulo(capitulo, atualizar):
    espaco = {"__name__": "__main__"}
    problemas = []
    for arquivo in sorted((PASTA / capitulo).glob("*.py")):
        destino = SAIDAS / capitulo / (arquivo.stem + ".txt")
        codigo = arquivo.read_text(encoding="utf-8")
        if "_rede" in arquivo.stem and destino.exists() and not atualizar:
            print(f"  {arquivo.name}: dados já baixados (use --atualizar para baixar de novo)")
            continue
        buffer = io.StringIO()
        with warnings.catch_warnings(record=True) as avisos, contextlib.redirect_stdout(buffer):
            warnings.simplefilter("always")
            try:
                exec(compile(codigo, str(arquivo), "exec"), espaco)
            except Exception as erro:
                if "_erro" not in arquivo.stem:
                    traceback.print_exc(file=sys.stderr)
                    problemas.append(f"{arquivo.name}: ERRO {type(erro).__name__}: {erro}")
                print(f"{type(erro).__name__}: {erro}")
        plt.close("all")
        saida = buffer.getvalue().rstrip("\n")
        destino.parent.mkdir(parents=True, exist_ok=True)
        if saida:
            destino.write_text(saida + "\n", encoding="utf-8")
        elif destino.exists():
            destino.unlink()
        for aviso in avisos:
            problemas.append(f"{arquivo.name}: AVISO {aviso.category.__name__}: {aviso.message}")
        for nome, texto in (("código", codigo), ("saída", saida)):
            ruins = caracteres_invalidos(texto)
            if ruins:
                problemas.append(f"{arquivo.name}: caracteres não suportados na {nome}: {ruins}")
        largas = [l for l in codigo.splitlines() if len(l) > 76]
        largas += [l for l in saida.splitlines() if len(l) > 78]
        if largas:
            problemas.append(f"{arquivo.name}: {len(largas)} linha(s) longa(s) demais")
        print(f"  {arquivo.name}: {len(saida.splitlines())} linha(s) de saída")
    return problemas


def main():
    argumentos = sys.argv[1:]
    atualizar = "--atualizar" in argumentos
    capitulos = [a for a in argumentos if a.startswith("cap")] or sorted(
        p.name for p in PASTA.glob("cap[0-9][0-9]") if p.is_dir())
    problemas = []
    for capitulo in capitulos:
        print(capitulo)
        problemas += executar_capitulo(capitulo, atualizar)
    print("\nProblemas:" if problemas else "\nNenhum problema encontrado.")
    for p in problemas:
        print("  -", p)
    return 1 if any("ERRO" in p for p in problemas) else 0


if __name__ == "__main__":
    import os
    os.chdir(PASTA)  # as listagens usam caminhos relativos a esta pasta
    sys.exit(main())
