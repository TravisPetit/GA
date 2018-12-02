from functions import powerset, is_clique

def naive(V, E):
    """ Returns the biggest clique in V """
    for subset in powerset(V):
        if is_clique(subset, E):
            return subset
