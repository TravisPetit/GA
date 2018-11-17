import functions as fun

#V = [1,2]
#E = [{1,2}]

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
            pass
