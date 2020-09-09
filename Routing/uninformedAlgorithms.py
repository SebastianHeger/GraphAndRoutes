import random


def dijksta(graph):
    node_start = random.choice(list(graph.nodes.keys()))
    node_target = random.choice(list(graph.nodes.keys()))
    print(f'Route planning from {node_start} to {node_target} with Dijkstra-Algorithm.')

    weight_list = {node: 0 for node in graph.nodes}
    precursor_list = {node: None for node in graph.nodes}
    queue = [[node_start, 0]]
    closed_list = list()

    node_active = queue[0][0]
    weight_list[node_active] = 0

    # while node_active != node_target:
    #     node_active = queue[0][0]
    #     del queue[0]
    #     closed_list.append(node_active)
    #     neighbors = graph.edges[node_active]
    #     neighbors = [x for x in neighbors if x not in closed_list]
    #
    #     for neighbor in neighbors:
    #         # Berechnung der Kosten:
    #         cost = weight_list[node_active] + BasicMath.distance(graph.nodes[neighbor], graph.nodes[node_active])
    #
    #         # Status, ob Nachbar in queue:
    #         in_queue = False
    #         queue_element_temp = []
    #         for queue_element in queue:
    #             if queue_element[0] == neighbor:
    #                 in_queue = True
    #                 queue_element_temp = queue_element
    #                 break
    #
    #         if in_queue:
    #             if cost < queue_element_temp[1]:
    #                 queue.remove(queue_element_temp)
    #                 queue.append([neighbor, cost])
    #                 precursor_list[neighbor] = node_active
    #                 weight_list[neighbor] = weight_list[node_active] + \
    #                                         BasicMath.distance(graph.nodes[neighbor], graph.nodes[node_active])
    #
    #         else:
    #             queue.append([neighbor, cost])
    #             precursor_list[neighbor] = node_active
    #             weight_list[neighbor] = weight_list[node_active] + \
    #                                     BasicMath.distance(graph.nodes[neighbor], graph.nodes[node_active])
    #
    #     queue.sort(key=lambda x: x[1])
    #
    # # Pfad:
    # path = [end]
    # node_active = end
    # while node_active != start:
    #     node_active = precursor_list[node_active]
    #     path.append(node_active)
    #
    # cost = weight_list[end]
    # return path, cost