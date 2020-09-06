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
