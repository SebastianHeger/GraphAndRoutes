from pathlib import Path
import sqlite3
import random

from Graph import graphCreation
from Routing import uninformedAlgorithms, informedAlgorithms


if __name__ == '__main__':
    db_path = Path() / 'database.db'
    with sqlite3.connect(db_path) as db:
        graph = graphCreation.Graph(
            db=db,
            reinit=False,
            graph_accuracy=10
        )
        graph.generate_graph_output(
            image_filepath_input=Path() / 'Input' / 'MAP.png',
            image_filepath_output=Path() / 'Output' / 'GRAPH.png'
        )
        node_start = random.choice(list(graph.nodes.keys()))
        node_target = random.choice(list(graph.nodes.keys()))
        path, cost = uninformedAlgorithms.dijksta(
            graph=graph,
            node_start=node_start,
            node_target=node_target
        )
        informedAlgorithms.a_star(
            graph=graph,
            node_start=node_start,
            node_target=node_target
        )
