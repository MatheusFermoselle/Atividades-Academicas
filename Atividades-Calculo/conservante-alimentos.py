import statsmodels.api as sm
import numpy as np
import statistics as st


#1. Plote um gráfico de dispersão para decidir se uma reta pode descrever de modo razoável o comportamento geral dos dados
import matplotlib.pyplot as plot
x1 = np.array([36,82,45,49,21,24,58,73,85,52])
y1 = np.array([6,14,5,13,5,8,14,11,18,6])

plot.scatter(x1, y1, label='')
plot.plot(x1, y1, label='', color='red')
plot.xlabel('Eixo: X')
plot.ylabel('Eixo: Y')
plot.legend()
plot.title('conservante de alimentos ')
plot.grid()
plot.show()
a, b = st.linear_regression(x1, y1)
print(f"eq. da reta: y = {a:.2f}x + {b:.2f}")


print("---------------------------------------------------")

#2. Calcule a regressão linear dos dados e plote essa linha no gráfico de dispersão.
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

print("---------------------------------------------------")
#3. Use a equação de regressão para estimar a medida de hiperatividade de uma dessas crianças que ingeriu 65 gramas de comida com o conservante 45 minutos antes
x4 = np.array([0,45])
y4 = np.array([0,65])
x_const = sm.add_constant(x4)
modelo = sm.OLS(y4, x_const)
resultado = modelo.fit()
a1, b1 = resultado.params
print(f"eq. da reta: y = {a1:.2f}x + {b1:.2f}")

print("--------------------------------------------------")

 #4. Discuta os valores encontrados e a precisão da reta construída

 #R: Calculando a regressão linear para estimar a medida de hiperatividade de uma dessas crianças que ingeriu 65 gramas de comida com o conservante 45 minutos antes,
 # é possível observar que o coeficiente angular resulta em 0, mostrando que esta é uma reta constante. Além disso, no segundo gráfico percebemos que a reta se distancia 
 # dos pontos do gráfico, alertando um alto valor para o valor de R.


