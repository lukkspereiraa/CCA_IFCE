import random
import time

def buscaBinaria(lista, chave, inicio, fim):
    while inicio < fim:
        meio = (inicio + fim) // 2
        if lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio
    return inicio

def insertionSortOtimizado(lista):
    n = len(lista)
    
    for i in range(1, n):
        chave = lista[i]

        posicao = buscaBinaria(lista, chave, 0, i)

        lista = lista[:posicao] + [chave] + lista[posicao:i] + lista[i+1:]
        
    return lista

arrayDesordenado = random.sample(range(1, 1000), 100)
print(f"Numeros Desordenados: {arrayDesordenado}")

start = time.time()
arrayOrdenado = insertionSortOtimizado(arrayDesordenado)
end = time.time()
time_in_milliseconds = (end - start) * 1000

print(f"Numeros Ordenados: {arrayOrdenado}")
print(f"Tempo de execução: {time_in_milliseconds:.2f} ms")
