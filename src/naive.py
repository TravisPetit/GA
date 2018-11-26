import functions as fun

def naive(V, E):
    """ Returns the biggest clique in V """
    max_set = []
    pset = fun.powerset(V)
    for subset in pset:
        if fun.is_clique(subset, E) and len(subset) > len(max_set):
           max_set = subset
    return max_set
