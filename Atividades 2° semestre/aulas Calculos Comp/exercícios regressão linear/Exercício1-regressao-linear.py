import statistics as st
import numpy as np
# Exercício 1 
# a)
set1 = [2.9, 4.2, 3.2, 3.8, 4.0, 4.5, 3.4, 3.7, 2.1, 4.7,4.3,2.7,2.5,4.1,2.3,3.5,3.2,3.6]
print("a mediana dos rendimentos do título é {:.02f}".format(st.median(set1)))
print("a média dos rendimentos do título é {:.02f}".format(st.mean(set1)))
print("o desvio padrão dos rendimentos do título é {:.02f}".format(st.pstdev(set1)))
print("----------------------------------------------------------")
# b)
set2 = [18, 5, 11, 9, 14, 6, 13, 8, 22, 15,7,20,19,16,21,10,17,12]

a = np.array([[5,1],[9,1]])
b = np.array([4.2, 3.8])
solucao = np.linalg.solve(a, b)
print(solucao)
print("----------------------------------------------------------")
# c)
# R: Por conta da diferença entre os coeficientes podemos considerar que o sistema não é linear.
# d)
# R: Com base na análise do gráfico é recomendado que os investidores retirem suas aplicações, já que é um investimento instável e que está desvalorizando nos últimos anos. 

