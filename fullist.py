import networkx as nx
import matplotlib.pyplot as plt
import collections
from collections import deque
import csv

cities = open('cities.csv' , 'r', encoding ='utf-8')
reader = csv.reader(cities, delimiter=',', quotechar='"')
for index, row in enumerate(reader):
    if index>100:
        break
    print(row)

def shortest_path(G, city1, city2):
    way = nx.shortest_path(G, city1, city2, weight='weight')
    length = nx.shortest_path_length(G, city1, city2, weight='weight')
    return way, length

def find_shortest_path(G, start, end):
    dist = {start: [start]}
    q = deque([start])
    while len(q):
        at = q.popleft()
        for next in G[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist.get(end)
G=nx.Graph()
for edge in cities:
    G.add_edge(edge[0], edge[1], weight=edge[2])
print(nx.shortest_path(G, 'Chernihiv','Yahotyn', weight='weight'))
print(nx.shortest_path_length(G, 'Chernihiv','Yahotyn', weight='weight'))
nx.draw_networkx(G)