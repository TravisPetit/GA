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

x = naive()
print(x)
