def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivor = arr[-1]

    elementos_maiores = []
    elementos_menores = []

    for x in arr[:-1]:
        if x <=pivor:
            elementos_menores.append(x)
        else:
            elementos_maiores.append(x)
    
    return quick_sort(elementos_menores) + [pivor] + quick_sort(elementos_maiores)

arr = [12,31,34,412,2,67,12]
vetor_ordenado = quick_sort(arr)

print(f"lista ordenada {vetor_ordenado}")