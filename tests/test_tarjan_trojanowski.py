from tarjan_trojanowski import maxset
from functions import generate_graph_of_degree, complement, generate_random_graph
from naive import naive
from random import randint
import unittest

class TestTarjanTrojanowski(unittest.TestCase):

    def test_degree0(self):
        for i in range(3):
            V,E = generate_graph_of_degree(0)
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_degree1(self):
        for i in range(3):
            V,E = generate_graph_of_degree(1)
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_degree2(self):
        for i in range(3):
            V,E = generate_graph_of_degree(2)
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_degree3(self):
        for i in range(3):
            V,E = generate_graph_of_degree(3)
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_degree4(self):
        for i in range(3):
            V,E = generate_graph_of_degree(4)
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_degree5(self):
        for i in range(3):
            V,E = generate_graph_of_degree(5)
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_degree6(self):
        for i in range(3):
            V,E = generate_graph_of_degree(6)
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_degree7_and_higher(self):
        for i in range(3):
            V,E = generate_graph_of_degree(randint(7,25))
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


    def test_random_graph(self):
        for i in range(3):
            V,E = generate_random_graph()
            Ec = complement(V,E)
            expected = len(naive(V, Ec))
            actual = maxset(V,E)
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
