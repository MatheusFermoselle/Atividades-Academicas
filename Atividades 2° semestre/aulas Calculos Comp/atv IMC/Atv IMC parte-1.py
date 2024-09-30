peso=float(input('Quanto você pesa em Kg? (kg) '))
altura=float(input('Quanto você mede em altura? (m)'))
IMC = peso/(altura**2)
print('O seu IMC é de {:.1f}'.format(IMC))
