import functions as fun
import unittest

class TestFunctions(unittest.TestCase):

    @classmethod
    def setUp(self):
        global V, S, E
        V = [1,2,3,4,5,6,7,8,9,10]
        S = [1,3,9,2]
        E = [{1,3}, {1,9}, {1,2}, {3,9}, {3,2}, {9,2}, {2, 10}, {3, 10}]


    def test_powerset(self):
        X = fun.powerset(V)
        self.assertIn({1,2}, X)
        self.assertIn(set(), X)
        self.assertNotIn([{1,2,3}], X)


    def test_is_clique(self):
        self.assertTrue(fun.is_clique(S, E))
        self.assertFalse(fun.is_clique([1,4,5], E))
        self.assertTrue(fun.is_clique([], E))


    def test_asymetric_tuples(self):
        X = fun.asymetric_tuples(V)
        self.assertIn({1,3}, X)
        self.assertNotIn({3,3}, X)
        self.assertNotIn({1,2,3}, X)


    def test_G_complement(self):
        Ec = fun.G_complement(V, E)
        self.assertIn({7,8}, Ec)
        self.assertNotIn({1,2}, Ec)


    def test_adjacent(self):
        X = fun.adjacent(3, V, E)
        self.assertEqual(X, [1,2,9,10])


    def test_degree(self):
        X = fun.adjacent(3, V, E)
        self.assertEqual(fun.degree(3, V, E), 4)


    def test_conected_components(self):
        X = fun.connected_components(V, E)
        self.assertListEqual(X, [[1,2,3,9,10],[4],[5],[6],[7],[8]])
        X = fun.connected_components([], [])
        self.assertListEqual(X, [])


    def test_induced(self):
        X = fun.induced(V, E)
        #self.assertListEqual


if __name__ == '__main__':
    unittest.main()
