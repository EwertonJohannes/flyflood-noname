def ler_coordenadas_do_arquivo(nome_do_arquivo):
    coordenadas_dos_pontos = {}
    with open(nome_do_arquivo, 'r') as arquivo:
        next(arquivo)
        linhas_do_arquivo = arquivo.readlines()

        for numero_da_linha, linha_de_texto in enumerate(linhas_do_arquivo):
            elementos = linha_de_texto.strip().split()
            for numero_da_coluna, caractere in enumerate(elementos):
                if caractere != '0':
                    coordenadas_dos_pontos[caractere] = (numero_da_linha, numero_da_coluna)

    return coordenadas_dos_pontos

def gerar_permutacoes(lista_de_elementos):
    if len(lista_de_elementos) == 0:
        return [[]]

    todas_as_sequencias = []

    for indice in range(len(lista_de_elementos)):
        elemento_atual = lista_de_elementos[indice]
        elementos_restantes = lista_de_elementos[:indice] + lista_de_elementos[indice + 1:]
        sequencias_dos_restantes = gerar_permutacoes(elementos_restantes)

        for uma_sequencia in sequencias_dos_restantes:
            todas_as_sequencias.append([elemento_atual] + uma_sequencia)

    return todas_as_sequencias

def calcular_distancias(coordenadas, pontos_de_entrega):
    distancias = {}
    for i in pontos_de_entrega:
        for j in pontos_de_entrega:
            if i != j:
                distancias[f'{i+j}'] = abs(coordenadas[i][0] - coordenadas[j][0]) + abs(coordenadas[i][1] - coordenadas[j][1])
    return distancias

def calcular_distancias_r(coordenadas, pontos_de_entrega):
    distancias_r = {}
    for i in pontos_de_entrega:
        distancias_r[i] = abs(coordenadas['R'][0] - coordenadas[i][0]) + abs(coordenadas['R'][1] - coordenadas[i][1])
    return distancias_r

def calcular_percursos(coordenadas):
    distancias_percursos = {}
    pontos_de_entrega = []
    for i in coordenadas:
        if i != "R":
            pontos_de_entrega.append(i)
    distancias = calcular_distancias(coordenadas, pontos_de_entrega)
    distancias_r = calcular_distancias_r(coordenadas, pontos_de_entrega)
    permutacoes = gerar_permutacoes(pontos_de_entrega)

    for p in permutacoes:
        soma = 0
        for c in range(len(p) - 1):
            if (p[c] + p[c + 1]) in distancias:
                soma += distancias[p[c] + p[c + 1]]
        soma += distancias_r[p[0]] + distancias_r[p[-1]]
        distancias_percursos[f'{p}'] = soma
    return distancias_percursos

def encontrar_menor_caminho(coordenadas):
    menor_distancia_encontrada = float('inf')
    melhor_sequencia_encontrada = ""
    percursos = calcular_percursos(coordenadas)

    for i in percursos.values():
        if i < menor_distancia_encontrada:
            menor_distancia_encontrada = i
    for k in percursos.keys():
        if percursos[k] == menor_distancia_encontrada:
            melhor_sequencia_encontrada = k
    return melhor_sequencia_encontrada

if __name__ == '__main__':
    c = ler_coordenadas_do_arquivo('matriz.txt')
    sequencia = encontrar_menor_caminho(c)
    print(sequencia)
