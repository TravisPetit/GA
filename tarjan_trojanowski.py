import functions as fun
from math import floor

def maxset(V, E):
    """ Retruns the cardinality of the maximum independent set in (V,E) """

    if not V: # if V is empty
        return 0

    # -- STATEMENT 0 -- #
    components = fun.connected_components(V, E)
    if len(components) > 1: # if V is not connected
        temp = 0
        for connected_subgraph in components:
           temp += maxset(connected_subgraph, fun.induced(connected_subgraph, E))
        return temp

    v = fun.vertex_of_min_degree(V, E)

    # -- CASE: DEG = 0 -- #
    if fun.degree(v, V, E) == 0:
        temp = list( set(V) - {v} )
        return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 1 -- #
    elif fun.degree(v, V, E) == 1:
        Av = fun.adjacent(v, V, E)
        w = Av[0]
        temp = list(set(V) - {v,w})
        return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 2 -- #
    elif fun.degree(v, V, E) == 2:

    # -- STATEMENT 2.1 -- #
        if fun.for_all(V, lambda w: fun.degree(w, V, E) == 2):
            return floor( len(V) / 2 )
        else:
            w1 = list(filter(lambda x: fun.degree(x, V, E) >= 3 and {v, x} in E, fun.adjacent(v, V, E)))[0]
            w2 = list( set(fun.adjacent(v, V, E)) - {w1} )[0]

    # -- STATEMENT 2.2 -- #
        if {w1, w2} in E:
            temp = list(set(V) - {v,w1,w2})
            return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 2.3 -- #
        elif {w1, w2} not in E:
            temp1 = list(set(V) - {v,w1,w2})
            temp2 = list( set(V) - set(fun.adjacent(w1, V, E)) - set(fun.adjacent(w2, V, E)) )
            return max(1 + maxset(temp1, fun.induced(temp1, E)), 2 + maxset(temp2, fun.induced(temp2, E)))

    # -- STATMENT 3 -- #
    elif fun.degree(v, V, E) == 3:
        Av = fun.adjacent(v, V, E)
        w1, w2, w3 = Av[0], Av[1], Av[2]

    # -- STATEMENT 3.1 -- #
        if {w1,w2} in E and {w1,w3} in E and {w2,w3} in E:
            temp = list( set(V) - {v,w1,w2,w3} )
            return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 3.2 -- #
        if ({w1,w2} in E and {w1,w3} in E) or ({w1,w3} in E and {w2,w3} in E) or ({w1,w2} in E and {w2,w3} in E):
            temp1 = list( set(V) - {v,w1,w2,w3} )
            temp2 = list( set(V) - set(fun.adjacent(w2, V, E)) - set(fun.adjacent(w3, V, E)) )
            return max(1 + maxset(temp1, fun.induced(temp1, E)), 2 + maxset(temp2, fun.induced(temp2, E)))

    # -- STATEMENT 3.3 -- #
        if {w1,w2} in E or {w1,w3} in E or {w2,w3} in E:
            A1c = list( set(v) - {w1,w2,w3} - set(fun.adjacent(w1, V, E)) )
            A2c = list( set(v) - {w1,w2,w3} - set(fun.adjacent(w2, V, E)) )
            A3c = list( set(v) - {w1,w2,w3} - set(fun.adjacent(w3, V, E)) )
