import random


def a_star(graph):
    node_start = random.choice(list(graph.nodes.keys()))
    node_target = random.choice(list(graph.nodes.keys()))
    print(f'Route planning from {node_start} to {node_target} with Dijkstra-Algorithm.')

# weight_list = {node: 0 for node in graph.nodes}


#     precursor_list = {node: None for node in graph.nodes}
#
#     queue = [[start, 0]]
#     node_active = queue[0][0]
#     closed_list = list()
#     weight_list[node_active] = 0
#
#     while node_active != end:
#         # setze aktiven knoten und füge ihn der closed list hinzu
#         node_active = queue[0][0]
#         # print('Aktiver Knoten:', node_active)
#         del queue[0]
#         # print('Queue:', queue)
#
#         closed_list.append(node_active)
#         # print('Closed:', closed_list)
#         # suche nachbarknoten:
#         neighbors = graph.neighbors[node_active]
#         # print(neighbors)
#         neighbors = [x for x in neighbors if x not in closed_list]
#         # print('Neighbors:', neighbors)
#
#         for neighbor in neighbors:
#             # Berechnung der Kosten:
#
#             cost_to_start = weight_list[node_active] + BasicMath.distance(graph.nodes[neighbor],
#                                                                           graph.nodes[node_active])
#             cost_to_end = BasicMath.distance(graph.nodes[neighbor], graph.nodes[end])
#             cost = cost_to_start + cost_to_end
#             # print(cost, cost_to_start, cost_to_end)
#
#             # Status, ob Nachbar in queue:
#             in_queue = False
#             queue_element_temp = []
#             for queue_element in queue:
#                 if queue_element[0] == neighbor:
#                     in_queue = True
#                     queue_element_temp = queue_element
#                     break
#
#             if in_queue:
#                 if cost < queue_element_temp[1]:
#                     queue.remove(queue_element_temp)
#                     queue.append([neighbor, cost])
#                     precursor_list[neighbor] = node_active
#                     weight_list[neighbor] = weight_list[node_active] + BasicMath.distance(graph.nodes[neighbor],
#                                                                                           graph.nodes[node_active])
#
#             else:
#                 queue.append([neighbor, cost])
#                 precursor_list[neighbor] = node_active
#                 weight_list[neighbor] = weight_list[node_active] + BasicMath.distance(graph.nodes[neighbor],
#                                                                                       graph.nodes[node_active])
#
#         queue.sort(key=lambda x: x[1])
#
#     # Pfad:
#     path = [end]
#     node_active = end
#     while node_active != start:
#         node_active = precursor_list[node_active]
#         path.append(node_active)
#     path.reverse()
#     cost = weight_list[end]
#     return path, cost