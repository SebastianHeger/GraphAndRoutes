import math


def euklidian_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def a_star(graph, node_start, node_target):
    print(f'Route planning from {node_start} to {node_target} with A-Star-Algorithm...')
    edges = dict()
    for item in graph.edges:
        node_1 = graph.edges[item]['connection'][0]
        node_2 = graph.edges[item]['connection'][1]
        distance = graph.edges[item]['distance']

        if node_1 in edges:
            edges[node_1].append([node_2, distance])
        else:
            edges[node_1] = [[node_2, distance]]

        if node_2 in edges:
            edges[node_2].append([node_1, distance])
        else:
            edges[node_2] = [[node_1, distance]]

    weight_list = {node: 0 for node in graph.nodes}
    precursors = {node: None for node in graph.nodes}
    queue = [[node_start, 0]]
    closed_list = list()

    node_active = queue[0][0]
    weight_list[node_active] = 0

    while node_active != node_target:
        node_active = queue[0][0]
        del queue[0]
        closed_list.append(node_active)
        neighbors = edges[node_active]
        neighbors = [x for x in neighbors if x[0] not in closed_list]
        for neighbor, distance in neighbors:
            # state handling: neighbor in queue
            in_queue = False
            queue_element_temp = []
            for queue_element in queue:
                if queue_element[0] == neighbor:
                    in_queue = True
                    queue_element_temp = queue_element
                    break

            cost_to_start = weight_list[node_active] + distance
            cost_to_end = euklidian_distance(
                x1=graph.nodes[neighbor][0],
                y1=graph.nodes[neighbor][1],
                x2=graph.nodes[node_target][0],
                y2=graph.nodes[node_target][1]
            )
            cost = cost_to_start + cost_to_end

            if in_queue:
                if cost < queue_element_temp[1]:
                    queue.remove(queue_element_temp)
                    queue.append([neighbor, cost])
                    precursors[neighbor] = node_active
                    weight_list[neighbor] = weight_list[node_active] + distance

            else:
                queue.append([neighbor, cost])
                precursors[neighbor] = node_active
                weight_list[neighbor] = weight_list[node_active] + distance

        queue.sort(key=lambda x: x[1])

    path = [node_target]
    node_active = node_target
    while node_active != node_start:
        node_active = precursors[node_active]
        path.append(node_active)

    cost = weight_list[node_target]
    print(f'Route length {cost} calculated with A-Star-Algorithm!')
    return path, cost
