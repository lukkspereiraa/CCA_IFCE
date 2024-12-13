import random
import time

def bubbleSortOtimizado(array):
    tamanhoDoArray = len(array)

    for i in range(tamanhoDoArray - 1):
        houveTroca = False
        for j in range(tamanhoDoArray - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                houveTroca = True

        if not houveTroca:
            break
    return array

arrayDesordenado = random.sample(range(1, 1000), 100)
print("Lista de valores desordenada:")
print(arrayDesordenado)

start = time.time()
arrayOrdenado = bubbleSortOtimizado(arrayDesordenado)
end = time.time()
time_in_milliseconds = (end - start) * 1000

print("Lista de valores ordenadas:")
print(arrayOrdenado)
print(f"Tempo de execução: {time_in_milliseconds:.2f} ms")
