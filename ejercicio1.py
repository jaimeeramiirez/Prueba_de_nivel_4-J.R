import numpy as np
from heapq import heappop, heappush

# Definición de personajes y grafo
personajes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']
grafo = np.array([
  [0, 6, 0, 1, 8, 7, 3, 2],
  [6, 0, 0, 6, 1, 8, 9, 1],
  [0, 0, 0, 1, 2, 1, 5, 0],
  [1, 6, 1, 0, 1, 5, 9, 3],
  [8, 1, 2, 1, 0, 2, 4, 5],
  [7, 8, 1, 5, 2, 0, 1, 6],
  [3, 9, 5, 9, 4, 1, 0, 1],
  [2, 1, 0, 3, 5, 6, 1, 0]
])

# Algoritmo de Prim
def prim(grafo, inicio):
    n = len(grafo)
    visitados = [False]*n
    pesos = [-1]*n
    previos = [None]*n
    pesos[inicio] = 0
    cola_prioridad = [(0, inicio)]

    while cola_prioridad:
        peso, u = heappop(cola_prioridad)
        if not visitados[u]:
            visitados[u] = True
            for v, peso_uv in enumerate(grafo[u]):
                if not visitados[v] and (pesos[v] == -1 or pesos[v] < peso_uv):
                    pesos[v] = peso_uv
                    previos[v] = u
                    heappush(cola_prioridad, (peso_uv, v))
    return previos

# -----------------------------
# APARTADO A
# -----------------------------
print("\n---APARTADO A---")
inicio = personajes.index('Iron Man')
previos = prim(grafo, inicio)
print("Árbol de expansión máximo desde Iron Man:")
for i, p in enumerate(previos):
    if p is not None:
        print(f'{personajes[p]} -- {personajes[i]}')

# -----------------------------
# APARTADO B
# -----------------------------
print("\n---APARTADO B---")
max_episodios = np.max(grafo)
print(f'\nMáximo número de episodios compartidos: {max_episodios}')
print('Pares de personajes que comparten el máximo número de episodios:')
indices = np.where(grafo == max_episodios)
for i in range(len(indices[0])):
    if indices[0][i] < indices[1][i]:
        print(f'{personajes[indices[0][i]]} -- {personajes[indices[1][i]]}')

# -----------------------------
# APARTADO C
# -----------------------------
print("\n---APARTADO C---")
print('\nTodos los personajes:')
for personaje in personajes:
    print(personaje)

# -----------------------------
# APARTADO D
# -----------------------------
print("\n---APARTADO D---")
print('\nPersonajes que aparecieron en nueve episodios de la saga:')
indices_nueve_episodios = np.where(grafo == 9)
for i in range(len(indices_nueve_episodios[0])):
    if indices_nueve_episodios[0][i] < indices_nueve_episodios[1][i]:
        print(f'{personajes[indices_nueve_episodios[0][i]]} -- {personajes[indices_nueve_episodios[1][i]]}')
