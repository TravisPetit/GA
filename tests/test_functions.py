import functions as fun
import unittest
from random import shuffle

class TestFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global V, S, E
        V = {1,2,3,4,5,6,7,8,9,10}
        S = {1,3,9,2}
        E = [{1,3}, {1,9}, {1,2}, {3,9}, {3,2}, {9,2}, {2, 10}, {3, 10}]


    def setUp(self):
        shuffle(E)


    def test_powerset(self):
        X = fun.powerset(V)
        self.assertIn({1,2}, X)
        self.assertIn(set(), X)
        self.assertNotIn({1,2,3,11}, X)


    def test_is_clique(self):
        self.assertTrue(fun.is_clique(S, E))
        self.assertFalse(fun.is_clique({1,4,5}, E))
        self.assertTrue(fun.is_clique(set(), E))


    def test_asymetric_tuples(self):
        X = fun.asymetric_tuples(V)
        self.assertIn({1,3}, X)
        self.assertNotIn({3,3}, X)
        self.assertNotIn({1,2,3}, X)


    def test_complement(self):
        Ec = fun.complement(V, E)
        self.assertIn({7,8}, Ec)
        self.assertNotIn({1,2}, Ec)


    def test_adjacent(self):
        X = fun.adjacent(3, V, E)
        self.assertSetEqual(X, {1,2,9,10})


    def test_degree(self):
        X = fun.degree(3, V, E)
        self.assertEqual(X, 4)
        X = fun.degree(8, V, E)
        self.assertEqual(X, 0)


    def test_conected_components(self):
        X = fun.connected_components(V, E)
        self.assertEqual(len(X), len([{1,2,3,9,10},{4},{5},{6},{7},{8}]))
        for component in [{1,2,3,9,10},{4},{5},{6},{7},{8}]:
           self.assertIn(component, X)
        X = fun.connected_components(set(), [])
        self.assertListEqual(X, [])


    def test_induced(self):
        X = fun.induced(V, E)
        self.assertEqual(len(X), len(E))
        for edge in E:
            self.assertIn(edge, X)
        X = fun.induced(S, E)
        self.assertEqual(len(X), len([{1,3}, {1,9}, {1,2}, {3,9}, {3,2}, {9,2}]))
        for edge in [{1,3}, {1,9}, {1,2}, {3,9}, {3,2}, {9,2}]:
            self.assertIn(edge, X)


    def test_vertex_of_min_degree(self):
        X = fun.vertex_of_min_degree(V, E)
        self.assertTrue(X == 4 or X == 5 or X == 6 or X == 7 or X == 8)


    def test_for_all(self):
        X = fun.for_all(V, lambda v: v <= 10)
        self.assertTrue(X)
        X = fun.for_all(V, lambda v: v > 2)
        self.assertFalse(X)


    def test_graph_of_degree_n(self):
        for i in range(20):
            V,E = fun.generate_graph_of_degree(i)
            for v in V:
                self.assertLessEqual(fun.degree(v, V, E), i)


if __name__ == '__main__':
    unittest.main()
