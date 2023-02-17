import networkx as nx
import matplotlib.pyplot as plt

elist = [
            ['Chernihiv', 'Nosivka', 71],
            ['Nosivka',	'Oster', 78],
            ['Nosivka',	'Yahotyn', 81],
            ['Berezan',	'Nosivka', 70]
]
G = nx.Graph()
G.add_weighted_edges_from(elist)
nx.draw_networkx(G)
print(G)
print(nx.shortest_path(G, 'Chernihiv','Yahotyn', weight='weight'))
print(nx.shortest_path_length(G, 'Chernihiv','Yahotyn', weight='weight'))