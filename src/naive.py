import functions as fun

def naive(V, E):
    """ Returns the biggest clique in V """
    pset = fun.powerset(V)
    for subset in pset:
        if fun.is_clique(subset, E):
            return subset
    return set()
