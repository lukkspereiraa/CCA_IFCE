import random
import time

def selectionSortOtimizado(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array

arrayDesordenado = random.sample(range(1, 1000), 100)
print("Array original:", arrayDesordenado)

start = time.time()
arrayOrdenado = selectionSortOtimizado(arrayDesordenado)
end = time.time()
time_in_milliseconds = (end - start) * 1000

print("Array ordenado:", arrayOrdenado)
print(f"Tempo de execução: {time_in_milliseconds:.2f} ms")
