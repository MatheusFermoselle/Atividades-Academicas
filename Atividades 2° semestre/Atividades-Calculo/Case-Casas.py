import statsmodels.api as sm
import statistics as st
import numpy as np
import matplotlib.pyplot as plot
# 1. Encontre uma equação linear que permita prever o preço de venda médio de uma
#casa no bairro dado, em termos de número de quartos e do número de banheiros

x1 = np.array([3, 2, 4, 2, 3, 2, 5, 4])
x2 = np.array([2, 1, 3, 1, 2, 2, 3, 2])
y = np.array([143.800, 109.300, 158.800, 109.200, 154.700, 114.900, 188.400, 142.900])


# Variáveis independentes (X) e dependente (y)
x = np.array([[3, 2], [2, 1], [4, 3], [2, 1], [3, 2], [2,2], [5,3], [4,2]])
y = np.array([143.800, 109.300, 158.800, 109.200, 154.700, 114.900, 188.400, 142.900])
# Adicionando a constante (termo de intercepto)à matriz x
x_const = sm.add_constant(x)
# Criando e ajustando o modelo OLS (regressão múltipla)
modelo = sm.OLS(y, x_const)
resultado = modelo.fit()
# Exibindo o resumo do modelo ajustado
print(resultado.summary())
 
 #2. Caso eu queira uma casa com 3 quartos e 1 banheiro, quanto seria o preço estimado?
y = (16.7524 * 3) + (11.2345 * 1) + 65.4298
print(f"{y:.3f}")


