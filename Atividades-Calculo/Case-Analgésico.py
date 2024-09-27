import statsmodels.api as sm
import statistics as st
import numpy as np
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression

x1 = np.array([15, 15, 15, 15, 30, 30, 30, 30, 45, 45, 45, 45])
x2 = np.array([20, 20, 30, 30, 20, 20, 30, 30, 20, 20, 30, 30])
x3 = np.array([10,20,10,20,10,20,10,20,10,20,10,20])

#1. Calcule a equação de regressão, comentando sobre a qualidade da reta encontrada.
x = np.array([
    [15, 20, 10],
    [15, 20, 20],
    [15, 30, 10],
    [15, 30, 20],
    [30, 20, 10],
    [30, 20, 20],
    [30, 30, 10],
    [30, 30, 20],
    [45, 20, 10],
    [45, 20, 20],
    [45, 30, 10],
    [45, 30, 20]
])
y = np.array([47, 54, 58, 66, 59, 67, 71, 83, 72, 82, 85, 94])

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
params = model.params
print(f"Coeficientes: {params}")

print(model.summary())

# R:  Equação de regressão --> y = -2.3333 + (0.9 * x1) + (1.2667 * x2) + (0.9 * x3)
# R:  Como todos os coeficientes de x1, x2 e x3 são altamente significativos e possuem diferenças pequenas, podemos analisar que as variáveis explicativas são bons preditores da variável dependente y. 

print("----------------------------------------------------------------------------")

#2. Utilize essa equação para estimar a eficácia percentual média de cápsulas contendo 12,5 mg do medicamento A, 25 mg do medicamento B e 15 mg do medicamento C

novos_valores = np.array([1, 12.5, 25, 15])  

eficacia_estimativa = np.dot(novos_valores, params)
print(f"Eficácia percentual estimada: {eficacia_estimativa:.2f}%")