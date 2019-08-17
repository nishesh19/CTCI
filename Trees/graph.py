from collections import defaultdict


class Graph:

    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node1):
        for edges in list(self._graph.values):
            try:
                edges.remove(node1)
            except KeyError:
                pass

        try:
            del self._graph[node1]
        except KeyError:
            pass

    def bfs(self):
        pass

    def dfs(self):
        pass


graph = Graph(directed = True)

no = int(input())
