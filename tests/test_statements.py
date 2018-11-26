from tarjan_trojanowski import maxset
import unittest

class TestStatements(unittest.TestCase):

    def test_empty(self):
        X = maxset(set(), [])
        self.assertEqual(X, 0)


    def test_DEG_0(self):
        X = maxset({1,2,3}, [])
        self.assertEqual(X, 3)


    def test_ST_1(self):
        X = maxset({1,2}, [{1,2}])
        self.assertEqual(X, 1)


    def test_ST_2_1(self):
        X = maxset({1,2,3}, [{1,2}, {1,3}, {2,3}])
        self.assertEqual(X, 1)


    def test_ST_2_2(self):
        V = {1,2,3,4}
        E = [{1,2},{1,3},{2,3},{2,4},{3,4}]
        X = maxset(V,E)
        self.assertEqual(X, 2)


if __name__ == '__main__':
    unittest.main()
