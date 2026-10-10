# Retornos exatamente iguais a zero: preço repetido de um dia para o outro
zeros = r_sp[r_sp == 0]
print(zeros.groupby(zeros.index.year // 10 * 10).size())
print("Ibovespa:", (r_ibov == 0).sum(), "retornos iguais a zero")
