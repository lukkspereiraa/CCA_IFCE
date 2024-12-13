import random
import time

def bubbleSort(array):
    tamanhoDoArray = len(array)

    for i in range(tamanhoDoArray-1):
        for j in range(tamanhoDoArray-1-i):
            if array[j] > array[j+1]:
              array[j], array[j+1] = array[j+1], array[j]
    return array
    

arrayDesordenado = random.sample(range(1,1000),100)
print('Lista de valores desordenada ')
print(arrayDesordenado)
start = time.time()
arrrayOrdenado = bubbleSort(arrayDesordenado)
end = time.time()
time_in_milliseconds = (end - start)*1000
print('Lista de valores ordenadas')
print(arrrayOrdenado)
print(f'Tempo de execucao: {time_in_milliseconds:.2f} m/s')