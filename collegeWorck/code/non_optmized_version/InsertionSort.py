import random
import time
def insertionSort(lista):
    n = len(lista)
    
    for i in range(n):
        chave = lista[i]
        j = i - 1
        
        while (j >= 0 and lista[j] > chave):
            lista[j + 1] = lista[j]
            j = j - 1
            
        lista[j + 1] = chave
    return lista

arrayDesordenado = random.sample(range(1,1000),100)
print(f"Numeros Desordenados {arrayDesordenado}")
start = time.time()
arrayOrdenado = insertionSort(arrayDesordenado)
end = time.time()
time_in_milliseconds = (end - start)*1000
print(f"Numeros Ordenados {arrayOrdenado}")
print(f'Tempo de execucao: {time_in_milliseconds:.2f} m/s')