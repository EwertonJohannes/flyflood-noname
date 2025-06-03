def distancia(a, b):
    
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return (dx * dx + dy * dy) ** 0.5


def gerar_permutacoes(lista):
    if len(lista) <= 1:
        return [lista]
    
    permutacoes = []
    for i in range(len(lista)):
        resto = lista[:i] + lista[i+1:]
        for p in gerar_permutacoes(resto):
            permutacoes.append([lista[i]] + p)
    return permutacoes


def força_bruta(pontos, origem):
    indices = list(range(len(pontos)))
    todas_permutacoes = gerar_permutacoes(indices)

    menor_custo = float('inf')
    melhor_rota = []

    for perm in todas_permutacoes:
        custo = 0
        atual = origem

        
        custo += distancia(origem, pontos[perm[0]])

        
        for i in range(len(perm) - 1):
            custo += distancia(pontos[perm[i]], pontos[perm[i + 1]])

        
        custo += distancia(pontos[perm[-1]], origem)

        if custo < menor_custo:
            menor_custo = custo
            melhor_rota = perm

    return melhor_rota, menor_custo


pontos = [(1, 2), (4, 5), (9, 6)]
origem = (0, 0)

rota, custo = força_bruta(pontos, origem)

print("Melhor rota (índices):", rota)
