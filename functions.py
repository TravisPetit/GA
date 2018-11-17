from random import random, randint
import itertools

def powerset(S):
    """ Returns a list with all the possible subsets of S """
    powerset = []
    for n in range(len(S) + 1):
        for subset in itertools.combinations(S, n):
            subset = set(subset)
            powerset.append(subset)
    return powerset


def is_clique(S, E):
    """ Returns true if S is a clique in (V,E) """
    SxS = asymetric_tuples(S)
    for pair in SxS:
        if pair not in E:
            return False
    return True


def asymetric_tuples(S):
    """ Returns all possible subsets of S with cardinality 2 """
    temp = []
    for i in S:
        for j in S:
            if {i,j} not in temp and i != j:
                temp.append({i,j})
    return temp

# pretty but too complicated
#def asymetric_tuples(S):
#    return list(filter(lambda x : len(x) == 2, [{x,y} for x,y in zip(*[iter(S)]*2)]))


def G_complement(V, E):
    """ Returns E complement """
    temp = []
    VxV = asymetric_tuples(V)
    for pair in VxV:
        if not pair in E:
            temp.append(pair)
    return temp


def generate_random_graph():
    """ Used for testing purposes """
    V = [x for x in range (randint(5,25))]
    E = []
    for pair in asymetric_tuples(V):
        if random() > 0.5:
            E.append(pair)
    return V, E


def adjacent(v, V, E):
    """ Returns a list with all the vertices adjacent to v """
    return list(filter(lambda w : {v,w} in E, V))


def degree(v, V, E):
    """ Returns the number of adjacent vertices to v """
    return len(adjacent(v, V, E))


def connected_components(V, E):
    """ Returns a list of the connected_components components of V using DFS """
    visited = []
    components = []

    def dfs(node):
        for neighbour in adjacent(node, V, E):
            if neighbour not in visited:
                visited.append(neighbour)
                subgraph.append(neighbour)
                dfs(neighbour)

    for vertex in V:
        if vertex not in visited:
            visited.append(vertex)
            subgraph = [vertex]
            dfs(vertex)
            components.append(subgraph)
    return components


def induced(S, E):
    """ Returns G(S):= graph induced by S which is a subset of E """
    return list(filter(lambda pair: pair.issubset(set(S)) , E))


def vertex_of_min_degree(V, E):
    """ Returns a vertex of minumum degree """
    min_vertex = V[0]
    for vertex in V:
        if degree(vertex, V, E) < degree(min_vertex, V, E):
            min_vertex = vertex
    return min_vertex


def for_all(S, f):
    """ returns true if f evaluates to True for all inputs of S """
    for s in S:
        if not f(s):
            return False
    return True


V = [1,2,3,4,5]
E = [ {1,2}, {2,5}, {3, 4} ]
#print(induced(V,E))
