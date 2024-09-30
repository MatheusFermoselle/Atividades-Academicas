import psutil
import time
from datetime import datetime

contador = 1
lista_cap = []
while (contador <= 20):
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M:%S')
    mem = psutil.virtual_memory()
    print(f"Uso de memoria:",{mem.percent})
    time.sleep(5)
    contador = contador + 1
    dic1 = {"memória em porcentagem": mem.percent,"data e hora": data_e_hora_em_texto}
    print(dic1)
    lista_cap.append(dic1)

print("Itens da lista de dicionários: ")    
for lista in lista_cap:    
    print(lista)


        
