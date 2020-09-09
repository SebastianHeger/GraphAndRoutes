import random


class Dijksta:
    def __init__(self, graph):
        node_start = random.choice(list(graph.nodes.keys()))
        node_target = random.choice(list(graph.nodes.keys()))
        print(f'Route planning from {node_start} to {node_target} with Dijkstra-Algorithm.')
