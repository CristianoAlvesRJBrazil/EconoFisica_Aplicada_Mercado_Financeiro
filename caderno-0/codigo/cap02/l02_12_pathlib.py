from pathlib import Path

pasta = Path("dados") / "exemplo"
pasta.mkdir(parents=True, exist_ok=True)     # não reclama se já existir

arquivo = pasta / "fechamentos.txt"
arquivo.write_text("\n".join(str(p) for p in fechamentos), encoding="utf-8")
print(arquivo, arquivo.exists(), arquivo.stat().st_size, "bytes")
print(arquivo.read_text(encoding="utf-8").splitlines()[:3])
