import heapq  # Importação de heapq (não usado, mas útil para otimizações futuras)

def ordenar_atividades(atividades):
    """
    Ordena as atividades pelo horário de término para maximizar a seleção de atividades não sobrepostas.
    :param atividades: Lista de tuplas (inicio, fim) representando cada atividade.
    :return: Lista de atividades ordenadas pelo horário de término.
    """
    return sorted(atividades, key=lambda x: x[1])  # Ordena pelo segundo elemento da tupla (horário de término)

def alg_guloso(atividades):
    """
    Algoritmo guloso para selecionar o máximo de atividades sem sobreposição.
    :param atividades: Lista de atividades ordenadas pelo horário de término.
    :return: Lista de atividades selecionadas.
    """
    if not atividades:  # Verifica se a lista de atividades está vazia
        return []  # Retorna uma lista vazia se não houver atividades

    atvd_selecionadas = []  # Lista para armazenar as atividades escolhidas
    fim_ultima = 0  # Mantém o horário de término da última atividade selecionada

    # Percorre todas as atividades já ordenadas
    for inicio, fim in atividades:
        if inicio >= fim_ultima:  # Se a atividade não se sobrepõe à última selecionada
            atvd_selecionadas.append((inicio, fim))  # Adiciona a atividade à lista final
            fim_ultima = fim  # Atualiza o horário de término para evitar conflitos

    return atvd_selecionadas  # Retorna a lista das atividades escolhidas

# Lista de atividades com seus horários de início e término
atividades = [(2, 5), (5, 7), (6, 8), (1, 3), (4, 6)]

# Ordena as atividades pelo tempo de término
atividades_ordenadas = ordenar_atividades(atividades)

# Aplica o algoritmo guloso para selecionar atividades sem sobreposição
atividades_selecionadas = alg_guloso(atividades_ordenadas)

# Exibe a lista de atividades ordenadas
print("Atividades ordenadas:", atividades_ordenadas)

# Exibe a lista de atividades selecionadas pelo algoritmo guloso
print("Atividades selecionadas:", atividades_selecionadas)
