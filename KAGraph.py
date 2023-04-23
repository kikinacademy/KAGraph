class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes:
            self.nodes[node1] = {}
        if node2 not in self.nodes:
            self.nodes[node2] = {}
        self.nodes[node1][node2] = weight
        self.nodes[node2][node1] = weight

    def remove_edge(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            del self.nodes[node1][node2]
            del self.nodes[node2][node1]

    def get_neighbors(self, node):
        if node in self.nodes:
            return self.nodes[node].keys()

    def get_weight(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            return self.nodes[node1][node2]
         