from datetime import date, timedelta

inicio = date(2025, 1, 2)
fim = date(2025, 12, 30)
print((fim - inicio).days, "dias corridos")
print(inicio + timedelta(days=30))
print(inicio.strftime("%d/%m/%Y"), inicio.isoformat())
print(date.fromisoformat("2025-06-06").weekday())   # 0 = segunda-feira
