import functions as fun

#V = [1,2]
E = [{1,2}]

def maxset(V):
    """ Returns the cardinality of the maximum independent set in (V,E)
        Note E is a global variable. """
    global E

    # STATEMENT 0 #
    components = fun.connected_components(V,E)
    if len(components) > 1: # if V is not connected
        temp = 0
        for connected_subgraph in components:
           temp += maxset(connected_subgraph)
        return temp
    else:
        V.sort(fun.degree) # not quite working yet
        v = V[0]

    # STATEMENT 1 #
        if degree(v, V, E) == 1:
            Av = fun.adjacent(v)
        # ...
