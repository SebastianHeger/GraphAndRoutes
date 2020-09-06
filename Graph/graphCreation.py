from pathlib import Path
import math
import uuid

from PIL import Image


def database_reset(db):
    def delete_table(table_name):
        cur = db.cursor()
        cur.execute(f"DROP TABLE IF EXISTS {table_name} ")
        db.commit()

    def create_node_table():
        delete_table('nodes')
        cur = db.cursor()
        cur.execute(
            "CREATE TABLE nodes ("
            "id UUID PRIMARY KEY, "
            "pos_x INTEGER, "
            "pos_y INTEGER"
            ")"
        )
        db.commit()

    def create_edge_table():
        delete_table('edges')
        cur = db.cursor()
        cur.execute(
            "CREATE TABLE edges ("
            "id UUID PRIMARY KEY, "
            "node_1 UUID, "
            "node_2 UUID, "
            "distance REAL, "
            "FOREIGN KEY(node_1) REFERENCES nodes(id), "
            "FOREIGN KEY(node_2) REFERENCES nodes(id)"
            ")"
        )
        db.commit()

    create_node_table()
    create_edge_table()


class Graph:
    def __init__(self, db, reinit):
        self.nodes = dict()
        self.edges = dict()

        if reinit:
            database_reset(db)
            self.generate_graph(db)
        else:
            cur = db.cursor()
            for item in cur.execute('SELECT * FROM nodes'):
                self.nodes[item[0]] = [
                    item[1],
                    item[2]
                ]
            for item in cur.execute('SELECT * FROM edges'):
                self.edges[item[0]] = {
                    'connection': [
                        item[1],
                        item[2]
                    ],
                    'distance': item[3]
                }
            db.commit()

    def generate_graph(self, db, accuracy=5):
        def generate_nodes():
            cur = db.cursor()
            path = Path().parent / 'Input'
            filename = 'MAP.png'
            image = Image.open(path / filename, 'r')
            width, height = image.size
            steps_x = int(width / accuracy)
            steps_y = int(height / accuracy)

            for step_x in range(steps_x):
                for step_y in range(steps_y):
                    node_id = str(uuid.uuid4())
                    pos_x = int(step_x * accuracy + accuracy / 2)
                    pos_y = int(step_y * accuracy + accuracy / 2)
                    if image.getpixel((pos_x, pos_y)) == (0, 0, 0):
                        cur.execute("INSERT INTO nodes VALUES (?,?,?)", [node_id, pos_x, pos_y])
                        self.nodes[node_id] = [pos_x, pos_y]
            db.commit()
            print('Nodes created!')

        def generate_edges():
            def euklidian_distance(x1, y1, x2, y2):
                return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            cur = db.cursor()
            for node_id in self.nodes.keys():
                node_pos_x = self.nodes[node_id][0]
                node_pos_y = self.nodes[node_id][1]
                bound_x_lower = int(node_pos_x - (accuracy + math.sqrt(accuracy)))
                bound_x_upper = int(math.ceil(node_pos_x + (accuracy + math.sqrt(accuracy))))
                bound_y_lower = int(node_pos_y - (accuracy + math.sqrt(accuracy)))
                bound_y_upper = int(math.ceil(node_pos_y + (accuracy + math.sqrt(accuracy))))
                print(node_id, bound_x_lower, bound_x_upper, bound_y_lower, bound_y_upper)
                edge_list = list()
                for neighbor in cur.execute(
                    "SELECT * from nodes "
                    "WHERE pos_x BETWEEN ? AND ? "
                    "AND pos_y BETWEEN ? and ?; ",
                    (
                        bound_x_lower,
                        bound_x_upper,
                        bound_y_lower,
                        bound_y_upper
                    )
                ):
                    neighbor_id = neighbor[0]
                    if neighbor_id != node_id:
                        edge_id = str(uuid.uuid4())
                        neighbor_pos_x = self.nodes[neighbor_id][0]
                        neighbor_pos_y = self.nodes[neighbor_id][1]
                        distance = euklidian_distance(
                            node_pos_x,
                            node_pos_y,
                            neighbor_pos_x,
                            neighbor_pos_y)
                        edge_list.append([edge_id, node_id, neighbor_id, distance])
                for edge in edge_list:
                    cur.execute(
                        "INSERT INTO edges VALUES (?,?,?,?)",
                        [edge[0], edge[1], edge[2], edge[3]]
                    )
                    self.edges[edge[0]] = {
                        'connection': [
                            edge[1],
                            edge[2]
                        ],
                        'distance': edge[3]
                    }
            print('Edges created!')

        generate_nodes()
        generate_edges()
