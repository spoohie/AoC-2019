import networkx as nx

data = [i.split(')') for i in open('input.txt', 'r').read().splitlines()]
orbits = {planet[1]: [planet[0]] for planet in data}

graph = nx.DiGraph(orbits)

num = sum(len(nx.shortest_path(graph, planet, "COM")[1:]) for planet in graph.nodes())
print("1:", num)
