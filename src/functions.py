from random import random, randint, shuffle
from itertools import combinations

def powerset(S):
    """ Returns a list with all the possible subsets of S """
    powerset = []
    for n in range(len(S) + 1):
        for subset in combinations(S, n):
            subset = set(subset)
            powerset.append(subset)
    return powerset


def is_clique(S, E):
    """ Returns True if S is a clique E """
    SxS = asymetric_tuples(S)
    for pair in SxS:
        if pair not in E:
            return False
    return True


def asymetric_tuples(S):
    """ Returns all the possible subsets of S with cardinality 2 """
    temp = []
    for i in S:
        for j in S:
            if {i,j} not in temp and i != j:
                temp.append({i,j})
    return temp


def G_complement(V, E):
    """ Returns E complement """
    temp = []
    VxV = asymetric_tuples(V)
    for pair in VxV:
        if not pair in E:
            temp.append(pair)
    return temp


def generate_random_graph(p=0.5, lower = 1, upper=15):
    """ Generates a random graph using the Erdős–Rényi Model """
    V = {x for x in range (randint(lower, upper))}
    E = []
    for pair in asymetric_tuples(V):
        if p > random():
            E.append(pair)
    shuffle(E)
    return V, E


def generate_graph_of_degree(n):
    """ Generates a random graph where all the vertices have at most degree n """
    V = {x for x in range (randint(1,15))}
    E = []
    for pair in asymetric_tuples(V):
        temp = list(pair)
        u = temp[0]
        v = temp[1]
        if degree(u, V, E) < n and degree(v, V, E) < n and random() < 0.8:
            E.append(pair)
    shuffle(E)
    return V, E


def adjacent(v, V, E):
    """ Returns a set with all the vertices adjacent to v """
    return set(filter(lambda w : {v,w} in E, V))


def degree(v, V, E):
    """ Returns the number of adjacent vertices to v """
    return len(adjacent(v, V, E))


def connected_components(V, E):
    """ Returns a list of the connected components components of V using DFS """
    visited = set()
    components = []

    def dfs(node):
        for neighbour in adjacent(node, V, E):
            if neighbour not in visited:
                visited.add(neighbour)
                subgraph.add(neighbour)
                dfs(neighbour)

    for vertex in V:
        if vertex not in visited:
            visited.add(vertex)
            subgraph = {vertex}
            dfs(vertex)
            components.append(subgraph)
    return components


def induced(S, E):
    """ Returns E(S):= graph induced by S which is a subset of E """
    return list(filter(lambda pair: pair.issubset(set(S)) , E))


def vertex_of_min_degree(V, E):
    """ Returns a vertex of minumum degree """
    min_vertex = list(V)[0]
    for vertex in V:
        if degree(vertex, V, E) < degree(min_vertex, V, E):
            min_vertex = vertex
    return min_vertex


def for_all(S, f):
    """ returns True if f evaluates to True for all inputs of S """
    for s in S:
        if not f(s):
            return False
    return True

def density(V,E):
    """ Returns the graph density which is a number in the intervall [0,1] """
    if not V:
        return 0
    numerator = 2 * len(E)
    denominator = len(V) * (len(V) - 1)
    return numerator / denominator
