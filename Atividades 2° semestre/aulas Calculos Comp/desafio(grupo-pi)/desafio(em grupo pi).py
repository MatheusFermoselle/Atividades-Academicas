#Grupo 5: Eduardo Kendi - 03241063, Izabelle - 03241045, Matheus Fermoselle - 03241039, Pedro Antunes - 03241067, Pedro porfirio - 03241027 , Ruan  - 03241011

import psutil
import platform
import time
meu_so = platform.system()

print("SO que eu uso: ", meu_so)

memoria = psutil.virtual_memory()

disco = psutil.disk_usage("C:");

cpu = psutil.cpu_percent()


while True:
    print("-" * 50)
    mem = memoria.percent
    mem1 = memoria.percent
    mem2 = mem1 + (mem1 * 0.15)
    mem3 = mem2 / 1.05

    cpu1= cpu
    cpu2 = cpu1 + (cpu1 * 0.10)
    cpu3 = cpu2 / 0.95

    disc1 = disco.percent
    disc2 = disc1 - (disc1 * 0.05)
    disc3 = disc2 * 3

   
    maquina1 = {"CPU": cpu1, "Memória" : mem1, "Disco": disc1}
    maquina2 = {"CPU": cpu2, "Memória" : mem2, "Disco": disc2}
    maquina3 = {"CPU": cpu3, "Memória" : mem3, "Disco": disc3}
   
    print(f"Maquina 1: CPU: {maquina1["CPU"]:.2f}%; Memoria: {maquina1['Memória']:.2f}%; Disco: {maquina1['Disco']:.2f}%")
    print(f"Maquina 2: CPU: {maquina2["CPU"]:.2f}%; Memoria: {maquina2['Memória']:.2f}%; Disco: {maquina2['Disco']:.2f}%")
    print(f"Maquina 3: CPU: {maquina3["CPU"]:.2f}%; Memoria: {maquina3['Memória']:.2f}%; Disco: {maquina3['Disco']:.2f}%")
    print("-" * 50)
   
    time.sleep(2)
