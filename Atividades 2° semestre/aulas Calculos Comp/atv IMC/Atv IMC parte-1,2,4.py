peso=float(input('Quanto você pesa em Kg? (kg) '))
altura=float(input('Quanto você mede em altura? (m)'))
IMC = peso/(altura**2)
print('O seu IMC é de {:.2f}'.format(IMC))
if IMC < 18.5:
    print('Diagnóstico: Abaixo do peso normal')
elif(IMC >=18.5 and IMC <25):
    print('Diagnóstico: peso normal')
elif(IMC >=25 and IMC <30):
    print('Diagnóstico: sobrepeso')
elif(IMC >=30 and IMC <40):
    print('Diagnóstico: obeso')
elif(IMC >=40):
    print('Diagnóstico: obesidade mórbida')

#Pegunta 4: Alterar o número de casas decimais de 1 para 2, aumenta a precisão dos valores coletados.
