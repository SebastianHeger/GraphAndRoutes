from pathlib import Path
import sqlite3

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
        uninformedAlgorithms.dijksta(graph=graph)
        informedAlgorithms.a_star(graph=graph)
