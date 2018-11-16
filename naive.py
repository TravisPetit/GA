import functions as fun

V = [1, 2, 3, 4]
E = [{1,2}, {2,3}, {1,4}, {3,1}]

def naive(V, E):
    """ Returns the biggest clique in V """
    max_set = []
    pset = fun.powerset(V)
    for subset in pset:
        if fun.is_clique(subset, E) and len(subset) > len(max_set):
           max_set = subset
    return max_set

#x = naive(V, E)
#print(x)
