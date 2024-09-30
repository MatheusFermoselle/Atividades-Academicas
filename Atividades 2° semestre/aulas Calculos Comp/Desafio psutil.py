import psutil as p
contador = 0
while contador <= 20:
    mem = p.virtual_memory
    print("mem.percent")
