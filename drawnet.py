import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import rcParams
import gensim
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
# model = gensim.models.KeyedVectors.load_word2vec_format('jawiki.model.bin', binary=True)
model = gensim.models.KeyedVectors.load_word2vec_format('https://word2vecmodel.s3.ap-southeast-2.amazonaws.com/jawiki.model.bin', binary=True)

query = input('検索語を入力してください: ')
term1 = model.most_similar(str(query), topn=10)
G = nx.Graph()
# print(len(term1))
wg = len(term1)
for pair in term1 :
    G.add_edge(str(query), str(list(pair)[0]))
    G.edges[query, list(pair)[0]]['weight'] = list(pair)[1] * wg
    wg -= 1
# print(dict(G.nodes))
# print(dict(G.edges))
pos = nx.spring_layout(G, k=0.7)
edge_width = [d['weight']*1 for (u,v,d) in G.edges(data=True)]
# print(edge_width)
nx.draw_networkx_labels(G, pos=pos, font_family='sans-serif')
nx.draw_networkx_nodes(G, pos, alpha=0.5, node_size=1200)
nx.draw_networkx_edges(G, pos, width=edge_width, alpha=0.5)
plt.show()

