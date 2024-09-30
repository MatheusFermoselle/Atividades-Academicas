import statsmodels.api as sm
import statistics as st
import numpy as np
import matplotlib.pyplot as plot
# 1. Calcule o coeficiente angular da reta e seu coeficiente linear
x1 = np.array([2,7,9, 1, 5, 15])
y1 = np.array([13, 21, 23, 14, 15, 21])
a, b = st.linear_regression(x1, y1)
print(f"eq. da reta: y = {a:.2f}x + {b:.2f}")

#2. Use esse resultado para poder estimar quantos automóveis pode-se esperar que uma pessoa inspecione durante o mesmo período de duas horas se ela está trabalhando no posto de inspeção há oito semanas
ex2 = (0.67 * 8) + 13.46
print(ex2)
#R: Durante o mesmo período de 2 horas, caso a pessoa estivesse trabalhando durante 8 semanas, podemos ver que mantendo os resultados é esperado que ela inspecione 18 carros. 

#3. Exiba um gráfico com os dados e a reta de regressão formada
def formula(a,b,x):
    return a*x + b
def graph(a,b):
    x = x1
    y = formula(a,b,x)
    plot.scatter(x1,y1)
    plot.plot(x,y)
    plot.xticks(np.arange(5, 40, step = 5))
    plot.xlabel("usuários")
    plot.ylabel("uso da CPU [%]")
    plot.title("uso da cpu por usuário logado")
    plot.grid()
    plot.show()
graph(a, b)