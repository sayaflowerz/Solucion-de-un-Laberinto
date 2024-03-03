def matriz_a_grafo(laberinto):
    grafo = {}
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if laberinto[i][j] != 0:
                vecinos = []
                # Verificar celdas adyacentes
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(laberinto) and 0 <= nj < len(laberinto[0]) and laberinto[ni][nj] != 0:
                        vecinos.append((ni, nj))
                grafo[(i, j)] = vecinos
    return grafo

Laberinto = [
    [2, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 3, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
]

grafo = matriz_a_grafo(Laberinto)

def imprimir_grafo(grafo):
    for nodo, vecinos in grafo.items():
        print(f"Nodo {nodo}: Vecinos {vecinos}")

# Utilizamos la función para imprimir el grafo generado
imprimir_grafo(grafo)
