import functions as fun
import cases
from naive import naive
from math import floor

def maxset(V, E):
    """ Retruns the cardinality of the maximum independent set in (V,E) """

    # -- CASE: V={} -- #
    if not V:
        return 0

    # -- STATEMENT 0 -- #
    components = fun.connected_components(V, E)
    if len(components) > 1:
        temp = 0
        for connected_subgraph in components:
           temp += maxset(connected_subgraph, fun.induced(connected_subgraph, E))
        return temp
    v = fun.vertex_of_min_degree(V, E)

    # -- CASE: DEG=0 -- #
    if fun.degree(v, V, E) == 0:
        temp = V - {v}
        return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 1 -- #
    elif fun.degree(v, V, E) == 1:
        Av = fun.adjacent(v, V, E)
        w = list(Av)[0]
        temp = V - {v,w}
        return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 2 -- #
    elif fun.degree(v, V, E) == 2:

    # -- STATEMENT 2.1 -- #
        if fun.for_all(V, lambda w: fun.degree(w, V, E) == 2):
            return floor(len(V) / 2)
        else:
            v_, w1 = fun.n_k_degree(2, 3, V, E)
            w2 = list(fun.adjacent(v_, V, E) - {w1})[0]

    # -- STATEMENT 2.2 -- #
        if {w1, w2} in E:
            temp = V - {v_,w1,w2}
            return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 2.3 -- #
        elif {w1, w2} not in E:
            temp1 = V - {v_,w1,w2}
            # According to the paper this should be V - adj(w1) - adj(w2).
            # The authors seem to have forgotten about the - {w1} and - {w2}
            # because without them the algorithm does not work correctly
            temp2 = V - fun.adjacent(w1, V, E) - {w1} - fun.adjacent(w2, V, E) - {w2}
            return max(1 + maxset(temp1, fun.induced(temp1, E)), 2 + maxset(temp2, fun.induced(temp2, E)))

    # -- STATMENT 3 -- #
    elif fun.degree(v, V, E) == 3:
        Av = list(fun.adjacent(v, V, E))
        w1, w2, w3 = Av[0], Av[1], Av[2]

    # -- STATEMENT 3.1 -- #
        if {w1,w2} in E and {w1,w3} in E and {w2,w3} in E:
            temp = V - {v,w1,w2,w3}
            return 1 + maxset(temp, fun.induced(temp, E))

    # -- STATEMENT 3.2 Part 1 -- #
        elif {w1,w2} in E and {w1,w3} in E:
            temp1 = V - {v,w1,w2,w3}
            E1 = fun.induced(temp1, E)
            # Again, according to the paper the - {w2} and - {w3} should not be here
            # and yet these additions are necessary for the algorithm to work correctly
            temp2 = V - fun.adjacent(w2, V, E) - {w2} - fun.adjacent(w3, V, E) - {w3}
            E2 = fun.induced(temp2, E)
            return max(1 + maxset(temp1, E1), 2 + maxset(temp2, E2))

    # -- STATEMENT 3.2 Part 2 -- #
        elif {w1,w3} in E and {w2,w3} in E:
            temp1 = V - {v,w1,w2,w3}
            E1 = fun.induced(temp1, E)
            # Same thing here
            temp2 = V - fun.adjacent(w1, V, E) - {w1} - fun.adjacent(w2, V, E) - {w2}
            E2 = fun.induced(temp2, E)
            return max(1 + maxset(temp1, E1), 2 + maxset(temp2, E2))

    # -- STATEMENT 3.2 Part 3 -- #
        elif {w1,w2} in E and {w2,w3} in E:
            temp1 = V - {v,w1,w2,w3}
            E1 = fun.induced(temp1, E)
            # And here
            temp2 = V - fun.adjacent(w1, V, E) - {w1} - fun.adjacent(w3, V, E) - {w3}
            E2 = fun.induced(temp2, E)
            return max(1 + maxset(temp1, E1), 2 + maxset(temp2, E2))

    # -- STATEMENT 3.3 -- #
        elif {w1,w2} in E or {w1,w3} in E or {w2,w3} in E:
            A1c = V - {w1,w2,w3} - fun.adjacent(w1, V, E)
            A2c = V - {w1,w2,w3} - fun.adjacent(w2, V, E)
            A3c = V - {w1,w2,w3} - fun.adjacent(w3, V, E)

    # -- STATEMENT 3.3.1 -- #
            pass

    # -- STATEMENT 3.3.2 -- #
            if len(A1c & A3c) <= len(V) - 7 and len(A2c & A3c) <= len(V) - 7:
                   temp1 = V - {v,w1,w2,w3}
                   E1 = fun.induced(temp1, E)
                   temp2 = A1c & A3c
                   E2 = fun.induced(temp2, E)
                   temp3 = A2c & A3c
                   E3 = fun.induced(temp3, E)
                   return max(1 + maxset(temp1, E1), 2 + maxset(temp2, E2), 2 + maxset(temp3, E3))

    # -- STATEMENT 3.4 -- #
        elif {w1,w2} not in E and {w2,w3} not in E and {w1,w3} not in E:
            A1c = V - fun.adjacent(w1, V, E)
            A2c = V - fun.adjacent(w2, V, E)
            A3c = V - fun.adjacent(w3, V, E)

    # -- STATEMENT 3.4.1 -- #
            if len(A1c & A2c & A3c) >= len(V) - 7:
                temp1 = V - {v,w1,w2,w3}
                E1 = fun.induced(temp1, E)
                temp2 = V - (A1c & A2c & A3c)
                E2 = fun.induced(temp2, E)
                return max(1 + maxset(temp1, E1), 3 + maxset(temp2, E2))

    # -- STATEMENT 3.4.2 -- #
            elif len(A1c & A2c & A3c) == len(V) - 8 or len(A1c & A2c & A3c) == len(V) - 9:

    # -- STATEMENT 3.4.2.1 -- #
                if cases.case_3_4_2_1(A1c, A2c, A3c):
                    temp1 = V - {v,w1,w2,w3}
                    E1 = fun.induced(temp1, E)
                    temp2 = A1c & A2c & A3c
                    E2 = fun.induced(temp2, E)
                    return max(1 + maxset(temp1, E1), 3 + maxset(temp2, E2))

    # -- STATEMENT 3.4.2.2 -- #
                elif cases.case_3_4_2_2(A1c, A2c, A3c):
                    Aic, Ajc = fun.three_two_domination(A1c, A2c, A3c)
                    temp1 = V - {v,w1,w2,w3}
                    E1 = fun.induced(temp1, E)
                    temp2 = Aic & Ajc
                    E2 = fun.induced(temp2, E)
                    temp3 = A1c & A2c & A3c
                    E3 = fun.induced(temp3, E)
                    return max(1 + maxset(temp1, E1), 2 + maxset(temp2, E2), 3 + maxset(temp3, E3))

    # -- STATEMENT 3.4.3 -- #
            elif len(A1c & A2c & A3c) <= len(V) - 10:

    # -- STATEMENT 3.4.3.1 -- #
                if cases.case_3_4_3_1(A1c, A2c, A3c):
                    temp1 = V - {v,w1,w2,w3}
                    E1 = fun.induced(temp1, E)
                    temp2 = A1c & A2c & A3c
                    E2 = fun.induced(temp2, E)
                    return max(1 + maxset(temp1, E1), 3 + maxset(temp2, E2))

    # -- STATEMENT 3.4.3.2 -- #
                elif cases.case_3_4_3_2(A1c, A2c, A3c):
                    Aic, Ajc = fun.three_two_domination(A1c, A2c, A3c)
                    temp1 = V - {v,w1,w2,w3}
                    E1 = fun.induced(temp1, E)
                    temp2 = Aic & Ajc
                    E2 = fun.induced(temp2, E)
                    temp3 = A1c & A2c & A3c
                    E3 = fun.induced(temp3, E)
                    return max(1 + maxset(temp1, E1), 2 + maxset(temp2, E2), 3 + maxset(temp3, E3))

    # -- STATEMENT 3.4.3.3 -- #
                pass

    # -- STATEMENT 4 -- #
    elif fun.degree(v, V, E) == 4:

    # -- STATEMENT 4.1 -- #
        if fun.for_all(V, lambda w : fun.degree(w, V, E) == 4):
            pass

    # -- STATEMENT 4.2 -- #
        else:
            v_, w = fun.n_k_degree(4, 5, V, E)
            temp1 = V - {w} - fun.adjacent(w, V, E)
            E1 = fun.induced(temp1, E)
            temp2 = V - {w}
            E2 = fun.induced(temp2, E)
            return max(1 + maxset(temp1, E1), maxset(temp2, E2))

    # -- STATEMENT 5 -- #
    elif fun.for_all(V, lambda w : fun.degree(w, V, E) == 5):

    # -- STATEMENT 5.1 -- #
        if len(V) == 6:
            return 1

    # -- STATEMENT 5.2 -- #
        elif len(V) > 6:
            temp1 = V - {v} - fun.adjacent(v, V, E)
            E1 = fun.induced(temp1, E)
            temp2 = V - {v}
            E2 = fun.induced(temp2, E)
            return max(1 + maxset(temp1, E1), maxset(temp2, E2))

    # -- STATEMENT 6 -- #
    elif fun.degree(v, V, E) >= 6:
        temp1 = V - {v} - fun.adjacent(v, V, E)
        E1 = fun.induced(temp1, E)
        temp2 = V - {v}
        E2 = fun.induced(temp2, E)
        return max(1 + maxset(temp1, E1), maxset(temp2, E2))

    # Default case for non-implemented statements
    return len(naive(V, fun.complement(V, E)))
