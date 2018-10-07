import itertools

V = [1, 2, 3, 4]
E = [{1,2}, {2,3}, {1,4}, {3,1}]

def powerset(S):
    """ Returns a list with all the possible subsets of S """
    powerset = []
    for n in range(len(S) + 1):
        for subset in itertools.combinations(S, n):
            subset = set(subset)
            powerset.append(subset)
    return powerset

def is_clique(S):
    """ Returns true if S is a clique in V """
    SxS = asymetric_tuples(S)
    for tuple in SxS:
        if tuple not in E:
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

def naive():
    """ Returns the biggest clique in V """
    max_set = []
    pset = powerset(V)
    for subset in pset:
        if is_clique(subset) and len(subset) > len(max_set):
           max_set = subset
    return max_set

#x = naive()
#print(x)

#---------------

def G_complement():
    """ Sets the value of E to the E complement """
    global E
    temp = []
    VxV = asymetric_tuples(V)
    for tuple in VxV:
        if not tuple in E:
            temp.append(tuple)
    E = temp

def adjacent(v):
    """ Returns a list with all the vertices adjacent to v """
    #TODO
    #return list(filter(lambda w : {v,w} in E, E)) # :(
    pass

def degree(v):
    """ Returns the number of adjacent vertices to v """
    return len(adjacent(v))

#print(adjacent(1))
