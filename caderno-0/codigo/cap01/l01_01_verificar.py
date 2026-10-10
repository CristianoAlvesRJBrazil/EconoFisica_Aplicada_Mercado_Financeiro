import sys
from importlib.metadata import version

print("Python     ", sys.version.split()[0])
for pacote in ["numpy", "pandas", "scipy", "matplotlib", "yfinance",
               "python-bcb"]:
    print(f"{pacote:<11}", version(pacote))
