import statistics as st
import numpy as np
import matplotlib.pyplot as plt
# Exercício 1 
# a)
set1 = [2.9, 4.2, 3.2, 3.8, 4.0, 4.5, 3.4, 3.7, 2.1, 4.7,4.3,2.7,2.5,4.1,2.3,3.5,3.2,3.6]
print("Exercício 1")
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



# Exercício 2 
# a)
set1 = [200,190,175,171,168,150,148,140,131,127]
decis = np.percentile(set1,np.arange(0,101,10))

print("Exercício 2")
print("a moda dos valores de brilho é {:.02f}".format(st.mode(set1)))
print("a mediana dos valores de brilho é {:.02f}".format(st.median(set1)))
print(decis)
print("a variância dos valores de brilho é {:.02f}".format(st.pvariance(set1)))
print("o desvio padrão dos valores de brilho é {:.02f}".format(st.pstdev(set1)))
print("----------------------------------------------------------")
# b) 
set2 = [1/2, 1/4, 1/8, 1/15, 1/30, 1/60, 1/125, 1/250, 1/500, 1/1000]
plt.scatter(set1, set2, label='data')
plt.plot(set1, set2, label='fitted curve', color='red')
plt.xlabel('brilho da imagem')
plt.ylabel('configurações de abertura (%)')
plt.legend()
plt.title("Brilho da imagem vs Configurações de abertura")
plt.grid()
plt.show()

print("-------------------------------------------------------------")
# c)
a = np.array([[1/2,1],[1/4,1]])
b = np.array([200, 190])
solucao = np.linalg.solve(a, b)
print(solucao)
print("----------------------------------------------------------")

#d) As informações que pude obter com esse gráfico demonstram que o sistema é linear por conta da responsividade entre os dados apresentados.

#e) Eu recomendo que caso o fotógrafo queira um brilho específico, este, diminua a velocidade do(s) obturador(s), já que como podemos ver no gráfico os dados são diretamente proporcionais.
