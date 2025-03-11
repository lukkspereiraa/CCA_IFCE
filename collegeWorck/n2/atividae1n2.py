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
    if not atividades:
        return []

    atvd_selecionadas = [atividades[0]]  # Começa com a primeira atividade
    fim_ultima = atividades[0][1]  # Define o fim da primeira atividade selecionada

    for inicio, fim in atividades[1:]:  # Começa do segundo elemento
        if inicio >= fim_ultima:
            atvd_selecionadas.append((inicio, fim))
            fim_ultima = fim

    return atvd_selecionadas


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
