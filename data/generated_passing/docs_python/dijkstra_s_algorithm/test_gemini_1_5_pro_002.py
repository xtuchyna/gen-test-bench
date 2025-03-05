import unittest
from collections import namedtuple, deque
from pprint import pprint as pp

inf = float('inf')
Edge = namedtuple('Edge', ['start', 'end', 'cost'])

class Graph():
    def __init__(self, edges):
        self.edges = [Edge(*edge) for edge in edges]
        self.vertices = {e.start for e in self.edges} | {e.end for e in self.edges}

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))


        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:
                    dist[v] = alt
                    previous[v] = u

        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s


class TestDijkstra(unittest.TestCase):

    def setUp(self):
        self.graph = Graph([("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
                           ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
                           ("e", "f", 9)])

    def test_a_to_e(self):
        self.assertEqual(self.graph.dijkstra("a", "e"), deque(['a', 'c', 'd', 'e']))

    def test_a_to_f(self):
        self.assertEqual(self.graph.dijkstra("a", "f"), deque(['a', 'c', 'f']))

    def test_a_to_b(self):
        self.assertEqual(self.graph.dijkstra("a", "b"), deque(['a', 'b']))

    def test_a_to_c(self):
        self.assertEqual(self.graph.dijkstra("a", "c"), deque(['a', 'c']))
    
    def test_a_to_d(self):
        self.assertEqual(self.graph.dijkstra("a", "d"), deque(['a', 'c', 'd']))

    def test_b_to_e(self):  # Test a path starting from a different node
        self.assertEqual(self.graph.dijkstra("b", "e"), deque(['b', 'd', 'e']))

    def test_non_existent_node(self):
        with self.assertRaises(AssertionError):
            self.graph.dijkstra("g", "e")  # 'g' is not in the graph


if __name__ == '__main__':
    unittest.main()

