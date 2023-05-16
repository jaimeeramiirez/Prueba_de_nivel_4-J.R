import networkx as nx

# ---------------------------------------
# Apartado A: Carga de los datos
# ---------------------------------------

heroes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']

twitter_matrix = [
    [0, 75, 40, 16, 80, 20, 99, 23],
    [75, 0, 50, 67, 79, 38, 99, 41],
    [40, 50, 0, 17, 75, 52, 85, 28],
    [16, 67, 17, 0, 11, 50, 90, 36],
    [80, 79, 75, 11, 0, 26, 12, 56],
    [20, 38, 52, 50, 26, 0, 55, 61],
    [99, 99, 85, 90, 12, 55, 0, 10],
    [23, 41, 28, 36, 56, 61, 10, 0]
]

instagram_matrix = [
    [0, 61, 44, 66, 56, 74, 11, 65],
    [12, 0, 47, 41, 12, 38, 99, 41],
    [41, 23, 0, 45, 12, 89, 42, 14],
    [12, 69, 11, 0, 12, 50, 78, 63],
    [89, 19, 72, 11, 0, 26, 12, 56],
    [72, 34, 21, 65, 12, 0, 78, 41],
    [12, 87, 35, 99, 42, 15, 0, 10],
    [33, 41, 24, 61, 45, 41, 11, 0]
]

# ---------------------------------------
# Apartado B: Creación de los grafos
# ---------------------------------------

twitter_graph = nx.Graph()
instagram_graph = nx.Graph()

for i in range(len(heroes)):
    for j in range(i+1, len(heroes)):
        twitter_graph.add_edge(heroes[i], heroes[j], weight=twitter_matrix[i][j], label='Twitter') 
        instagram_graph.add_edge(heroes[i], heroes[j], weight=instagram_matrix[i][j], label='Instagram')

# ---------------------------------------
# Apartado C: Árbol de expansión máximo
# ---------------------------------------

# Note: NetworkX's maximum_spanning_tree function by default considers maximum weight edges first
max_tree_twitter = nx.maximum_spanning_tree(twitter_graph)
max_tree_instagram = nx.maximum_spanning_tree(instagram_graph)

# ---------------------------------------
# Apartado D: Conexión entre 'Captain America' y 'Nick Fury' en Twitter
# ---------------------------------------

has_path_twitter = nx.has_path(twitter_graph, 'Captain America', 'Nick Fury')

# ---------------------------------------
# Apartado E: Conexión entre 'The Winter Soldier' e 'Iron Man' en cualquier red social
# ---------------------------------------

has_path_social = nx.has_path(twitter_graph, 'The Winter Soldier', 'Iron Man') or nx.has_path(instagram_graph, 'The Winter Soldier', 'Iron Man')

# ---------------------------------------
# Apartado F: Personas que Thor sigue en Instagram
# ---------------------------------------

thor_follows = [n for n in instagram_graph.neighbors('Thor')]

# ---------------------------------------
# Impresión de los resultados
# ---------------------------------------

print("\n")
print(f"Árbol de expansión máximo para Twitter: {max_tree_twitter.edges(data=True)}") 
print("\n")
print(f"Árbol de expansión máximo para Instagram: {max_tree_instagram.edges(data=True)}")
print("\n")
print(f"¿Es posible conectar a Captain America con Nick Fury en Twitter?: {'Sí' if has_path_twitter else 'No'}")
print("\n")
print(f"¿Es posible conectar a The Winter Soldier con Iron Man en alguna red social?: {'Sí' if has_path_social else 'No'}")
print("\n")
print(f"Thor sigue a las siguientes personas en Instagram: {thor_follows}")
print("\n")