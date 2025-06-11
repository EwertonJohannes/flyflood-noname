def gerar_todas_as_permutacoes(lista_de_elementos):
    if len(lista_de_elementos) == 0:
        return [[]]

    todas_as_sequencias = []

    for indice in range(len(lista_de_elementos)):
        elemento_atual = lista_de_elementos[indice]
        elementos_restantes = lista_de_elementos[:indice] + lista_de_elementos[indice+1:]
        sequencias_dos_restantes = gerar_todas_as_permutacoes(elementos_restantes)

        for uma_sequencia in sequencias_dos_restantes:
            todas_as_sequencias.append([elemento_atual] + uma_sequencia)
            
    return todas_as_sequencias

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

def calcular_distancia_entre_pontos(coordenada_ponto_1, coordenada_ponto_2):
    linha_1, coluna_1 = coordenada_ponto_1
    linha_2, coluna_2 = coordenada_ponto_2
    distancia = abs(linha_1 - linha_2) + abs(coluna_1 - coluna_2)
    return distancia

def encontrar_menor_caminho_por_forca_bruta(coordenadas_de_todos_os_pontos):
    if 'R' not in coordenadas_de_todos_os_pontos:
        raise ValueError("Ponto de origem 'R' não foi encontrado na matriz.")

    coordenada_do_ponto_r = coordenadas_de_todos_os_pontos['R']
    pontos_para_entrega = {nome: coord for nome, coord in coordenadas_de_todos_os_pontos.items() if nome != 'R'}
    lista_de_nomes_dos_pontos_de_entrega = list(pontos_para_entrega.keys())

    menor_distancia_encontrada = float('inf')
    melhor_sequencia_encontrada = None

    todas_as_sequencias_possiveis = gerar_todas_as_permutacoes(lista_de_nomes_dos_pontos_de_entrega)

    for sequencia_atual in todas_as_sequencias_possiveis:
        distancia_da_sequencia_atual = 0
        coordenada_ponto_atual = coordenada_do_ponto_r
        nome_do_primeiro_ponto = sequencia_atual[0]
        coordenada_do_primeiro_ponto = pontos_para_entrega[nome_do_primeiro_ponto]
        distancia_da_sequencia_atual += calcular_distancia_entre_pontos(coordenada_ponto_atual, coordenada_do_primeiro_ponto)
        coordenada_ponto_atual = coordenada_do_primeiro_ponto

        for indice in range(len(sequencia_atual) - 1):
            nome_do_ponto_seguinte = sequencia_atual[indice+1]
            coordenada_do_ponto_seguinte = pontos_para_entrega[nome_do_ponto_seguinte]
            distancia_da_sequencia_atual += calcular_distancia_entre_pontos(coordenada_ponto_atual, coordenada_do_ponto_seguinte)
            coordenada_ponto_atual = coordenada_do_ponto_seguinte
            
        distancia_da_sequencia_atual += calcular_distancia_entre_pontos(coordenada_ponto_atual, coordenada_do_ponto_r)

        if distancia_da_sequencia_atual < menor_distancia_encontrada:
            menor_distancia_encontrada = distancia_da_sequencia_atual
            melhor_sequencia_encontrada = sequencia_atual
            
    return melhor_sequencia_encontrada, menor_distancia_encontrada

if __name__ == "__main__":
    nome_do_arquivo_de_entrada = 'matriz.txt'

    try:
        coordenadas = ler_coordenadas_do_arquivo(nome_do_arquivo_de_entrada)
        print(f"Pontos encontrados e suas coordenadas: {coordenadas}")

        sequencia_otima, distancia_minima = encontrar_menor_caminho_por_forca_bruta(coordenadas)

        if sequencia_otima:
            texto_da_sequencia = " ".join(sequencia_otima)
            
            print(f"A melhor sequência de entrega é: {texto_da_sequencia}")
        else:
            print("Não foi possível encontrar um caminho (não há pontos de entrega).")
    except FileNotFoundError:
        print(f"\nERRO: O arquivo '{nome_do_arquivo_de_entrada}' não foi encontrado.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")
