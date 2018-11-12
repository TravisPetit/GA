import functions as fun, unittest

class TestFunctions(unittest.TestCase):

    def test_is_clique(self):
        S = [1,3,2]
        E = [{1,2}, {3,1}, {3,2}]
        self.assertTrue(fun.is_clique(S, E))

    def test_empty_set_is_clique(self):
        S = []
        E = [{1,2}, {3,1}, {3,2}]
        self.assertTrue(fun.is_clique(S, E))


if __name__ == '__main__':
    unittest.main()
