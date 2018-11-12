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
    """ Returns true if S is a clique in V """
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


def G_complement(V, E):
    """ Sets the value of E to the E complement """
    temp = []
    VxV = asymetric_tuples(V)
    for pair in VxV:
        if not pair in E:
            temp.append(pair)
    return temp


def generate_random_graph():
    """ Used for testing purposes """
    size = randint(5, 25)
    counter = 0
    V = [x for x in range (size)]
    E = []
    for pair in asymetric_tuples(V):
        if random() > 0.5:
            E.append(pair)
            counter = counter + 1
    return V, E


def adjacent(v):
    """ Returns a list with all the vertices adjacent to v """
    #TODO
    #return list(filter(lambda w : {v,w} in E, E)) # :(
    pass

def degree(v):
    """ Returns the number of adjacent vertices to v """
    pass
    #return len(adjacent(v))

