import csv
import random
import time 
import os

Archivo_Numeros = "numeros_generados.csv"

if not os.path.exists(Archivo_Numeros):
    with open(Archivo_Numeros, mode='w', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        escritor.writerow(["Numero"])  

print("Generando números aleatorios entre 0 y 1 (sin incluir 0 ni 1)...")
print("Presiona Ctrl+C para detener el programa.")

try:
    with open(Archivo_Numeros, mode='a', newline='') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        
        while True:
            numero= random.uniform(0,1)
        
            if numero == 0 or numero == 1:
            
                continue
    
            escritor.writerow([numero])
            archivo_csv.flush()
            print(numero)
            time.sleep(0.3)
        
except KeyboardInterrupt:
    print("\n programa detenido con ctrl + c.") 