import functions as fun
from math import floor

def maxset(V, E):
    """ Returns the cardinality of the maximum independent set in (V,E) """

    # -- STATEMENT 0 -- #
    components = fun.connected_components(V, E)
    if len(components) > 1: # if V is not connected
        temp = 0
        for connected_subgraph in components:
           temp += maxset(connected_subgraph, fun.induced(connected_subgraph, E))
        return temp
    else:
        v = fun.vertex_of_min_degree(V, E)

    # -- STATEMENT 1 -- #
        if fun.degree(v, V, E) == 1:
            Av = fun.adjacent(v)
            w = Av[0]
            return 1 + maxset( list(set(V) - {v,w}) )

    # -- STATEMENT 2 -- #
        elif fun.degree(v, V, E) == 2:

    # -- STATEMENT 2.1 -- #
            if fun.for_all(V, lambda w: fun.degree(w, V, E) == 2):
                return floor( len(V) / 2 )
            else:
                w1 = list(filter(lambda x: fun.degree(x, V, E) >= 3 and {v, x} in E, fun.adjacent(v, V, E)))[0]
                w2 = list( set(fun.adjacent(v, V, E) - {w1}) )[0]

    # -- STATEMENT 2.2 -- #
            if {w1, w2} in E:
                return 1 + maxset( list(set(V) - {v,w1,w2}) )
