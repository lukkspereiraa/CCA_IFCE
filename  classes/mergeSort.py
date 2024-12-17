def mergeSort(arr):

    if len(arr) <= 1:
        return arr

    meio = len(arr)//2
    esquerda = mergeSort(arr[:meio])
    direita = mergeSort(arr[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    lista_ordenada = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            lista_ordenada.append(esquerda[i])
            i += 1
        else:
            lista_ordenada.append(direita[j])
            j += 1 
    
    lista_ordenada.extend(esquerda[i:])
    lista_ordenada.extend(direita[j:])

    return lista_ordenada

arr = [12,31,34,412,2,67,12]
print(f'Lista original {arr}')
lista_ordenada = mergeSort(arr)
print(f'lista  ordenada {lista_ordenada}')
