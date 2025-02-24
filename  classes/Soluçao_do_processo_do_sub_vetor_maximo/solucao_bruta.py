def Solucao_forca_bruta(vetor):
    tamanho_do_vetor = len(vetor)
    soma_maxima = float('-inf')
    inicio_max = 0
    fim_max = 0

    for i in range(tamanho_do_vetor):
        for j in range(i+1, tamanho_do_vetor):
            soma_ataual = sum(vetor[i:j + 1])
            if soma_ataual > soma_maxima:
                soma_maxima = soma_ataual
                inicio_max = i
                fim_max = j

    return soma_maxima , vetor[inicio_max:fim_max + 1]

vetor = [1, 21, -23, -3, 12, 23, 0, 12, 12, -2]

soma, subvetor = Solucao_forca_bruta(vetor)

print({f"soma maxima: {soma}"})
print({f"sub vetor: {subvetor}"})
