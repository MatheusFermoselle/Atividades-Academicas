import statsmodels.api as sm
import statistics as st
import numpy as np
import matplotlib.pyplot as plot
# Formule uma equação de regressão linear avaliando sua qualidade e buscando responder
# quantos sacos de trigo por hectare teríamos ao notar um índice pluviométrico de 9,5, 17,1
# e 6,8

x1 = np.array([12.9, 7.2, 11.3, 18.6, 8.8, 10.3, 15.9, 13.1])
y1 = np.array([62.5, 28.7, 52.2, 80.6, 41.6, 44.5, 71.3, 54.4])
a, b = st.linear_regression(x1, y1)
print(f"eq. da reta: y = {a:.2f}x + {b:.2f}")

y2 = 4.42 * 9.5 + 0.23
print(f"{y2:.1f}")
y3 = 4.42 * 17.1+ 0.23
print(f"{y3:.1f}")
y4 = 4.42 * 6.8 + 0.23
print(f"{y4:.1f}")