# Retornos sem laço: cada fechamento dividido pelo anterior
retornos = fechamentos[1:] / fechamentos[:-1] - 1
print(retornos.round(4))

log_retornos = np.diff(np.log(fechamentos))
print(log_retornos.round(4))
