import random
import time

def selectionSort(array):
    n  = len(array)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
            
        array[i], array[min_index] = array[min_index], array[i]


arrayDesordenado = random.sample(range(1,1000), 100)
print("Array original:", arrayDesordenado)
start = time.time()
arrayOrdenado = selectionSort(arrayDesordenado)
end = time.time()
time_in_milliseconds = (end - start)*1000
print("Array ordenado:", arrayOrdenado)
print(f'Tempo de execucao {time_in_milliseconds:.2f} m/s')