import statistics as st
import numpy as np


#Exercício 1
lista_usuarios= [10, 12, 15, 25, 22, 18, 15, 20, 28, 30]
print("a mediana do número de usuários é {}".format(st.median(lista_usuarios)))
print(f"a média do número de usuários é {st.mean(lista_usuarios)}")
print("O desvio padrão do número de usuários é {:.02f}".format(st.stdev(lista_usuarios)))


lista_cpu = [20.0, 25.2, 30.0, 45.1, 42.7, 33.6, 31.5, 45.0, 53.1, 60.2]
print("\na mediana do uso da CPU é {}".format(st.median(lista_cpu)))
print(f"a média do uso de CPU é {st.mean(lista_cpu)}")
print("O desvio padrão do uso de CPU é {:.02f}".format(st.stdev(lista_cpu)))

#Exercício 2

a = np.array([[10, 1], [15, 1]])
b = np.array([20.0, 30.0])
solucao1 = np.linalg.solve(a, b)
print(f"\n {solucao1}")

a2 = np.array([[12, 1], [25, 1]])
b2 = np.array([25.2, 45.1])
solucao2 = np.linalg.solve(a2, b2)
print(f"\n {solucao2}")

# É linear, já que o aumento do uso da CPU baseado no aumento do número de usuários é constante.
# A inclinação da amostra a é igual a 2 e a a interceptação é igual a 0. Já na outra amostra, a inclinação é 1.53 e a interceptação 6.83.


# Exercício 3

# y = ax + b
# 20 = a * 10 + b
# 20 = 2 * 10 + 0
# 20 = 20
