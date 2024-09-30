import statsmodels.api as sm
import statistics as st
import numpy as np
import matplotlib.pyplot as plot

x1 = np.array([0.02, 0.02, 0.10, 0.10, 0.18, 0.18])
x2 = np.array([1000, 1200, 1000, 1200, 1000, 1200])
y = np.array([78.9, 55.2, 80.9, 57.4, 85.3, 60.7])

x = np.array([[0.02, 1000], [0.02, 1200], [0.10, 1000], [0.10, 1200], [0.18, 1000], [0.18, 1200]])
y = np.array([78.9, 55.2, 80.9, 57.4, 85.3, 60.7])

# Adicionando a constante (termo de intercepto)à matriz x
x_const = sm.add_constant(x)
# Criando e ajustando o modelo OLS (regressão múltipla)
modelo = sm.OLS(y, x_const)
resultado = modelo.fit()
# Exibindo o resumo do modelo ajustado
print(resultado.summary())

print("-----------------------------------------------------------")


# 1. Ajuste uma equação da reta para os dados fornecidos
y1 = (37.1875 * x1) + (-0.1197 * x2) + 197.6479 

# 2. Utilize essa equação para estimar a dureza do aço quando o conteúdo de cobre é de 0,14% e a temperatura de têmpera for de 1100 F°
y2 = (37.1875 * 0.14) + (-0.1197 * 1100) + 197.6479 
print(f"{y2:.1f}")
