from tarjan_trojanowski import maxset
import unittest

class TestTarjanTrojanowski(unittest.TestCase):

    @classmethod
    def setUp(self):
        global V, E
        V = [1,2,3,4,5,6,7,8,9,10]
        E = [{1,3}, {1,9}, {1,2}, {3,9}, {3,2}, {9,2}, {2, 10}, {3, 10}]

    def test_global_V_E(self):
        X = maxset(V, E)
        self.assertIsNotNone(X)
        self.assertEqual(X, 7)

if __name__ == '__main__':
    unittest.main()
