import requests
import json
import collections
import itertools
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
from module import getAPI as api
from module import getTag as tag

mpl.rcParams['font.family'] = 'Hiragino Sans'
tags_list = tag.getTag(api.getApi())
tag_count = collections.Counter(
    itertools.chain.from_iterable(tags_list)).most_common(50)

G = nx.Graph()
G.add_nodes_from([(tag, {"count": count}) for tag, count in tag_count])

for gets in tags_list:
    for nda, ndb in itertools.combinations(gets, 2):
        if G.has_edge(nda, ndb):
            G[nda][ndb]["weight"] += 1
        if not G.has_node(nda) or not G.has_node(ndb):
            continue
        else:
            G.add_edge(nda, ndb, weight=1)

rem_list = []
for (u, v, d) in G.edges.data():
    if d["weight"] <= 4:
        rem_list.append((u, v))
for rem_edge in rem_list:
    a = rem_edge[0]
    b = rem_edge[1]
    G.remove_edge(a, b)

edge_width = [d["weight"]*0.2 for (u, v, d) in G.edges(data=True)]
pos = nx.spring_layout(G, k=1.0)
nx.draw_networkx_edges(
    G, pos, alpha=0.4, edge_color="maroon", width=edge_width)
node_size = [15*d["count"] for (n, d) in G.nodes(data=True)]
nx.draw_networkx_nodes(
    G, pos, alpha=0.6, node_color="gold", node_size=node_size)
nx.draw_networkx_labels(G, pos, font_size=9,
                        font_family="Hiragino Sans", font_weight="bold")
plt.axis('off')
plt.savefig("g2.png")
plt.show()
