import networkx as nx

# Definir el laberinto
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

# Crear un grafo dirigido
GrafoLaberinto = nx.Graph()

# Agregar nodos al grafo
for i in range(len(Laberinto)):
    for j in range(len(Laberinto[i])):
        if Laberinto[i][j] != 0:
            GrafoLaberinto.add_node((i, j))

# Agregar aristas al grafo
for i in range(len(Laberinto)):
    for j in range(len(Laberinto[i])):
        if Laberinto[i][j] != 0:
            # Verificar celdas adyacentes
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(Laberinto) and 0 <= nj < len(Laberinto[i]) and Laberinto[ni][nj] != 0:
                    GrafoLaberinto.add_edge((i, j), (ni, nj))

# Dibujar el grafo
nx.draw(GrafoLaberinto, with_labels=True)
