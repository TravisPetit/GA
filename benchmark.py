#from threading import *
from time import time
from naive import naive
from tarjan_trojanowski import maxset
from functions import generate_random_graph, density, G_complement

class Graph:

    def __init__(self, V, E):
        self.__E             = E
        self.__V             = V
        self.__density       = round(density(V, E), 4)
        self.__naive_time    = None
        self.__tar_troj_time = None


    def evaluate(self):
        start = time()
        naive(self.__V, self.__E)
        end = time()
        self.__naive_time = round(end - start, 4)

        start = time()
        Ec = G_complement(self.__V, self.__E)
        maxset(self.__V, Ec)
        end = time()
        self.__tar_troj_time = round(end - start, 4)


    def __repr__(self):
        temp =  "Vertices: "         + str(len(self.__V))        + "\n"
        temp += "Edges: "            + str(len(self.__E))        + "\n"
        temp += "Graph Density: "    + str(self.__density)       + "\n"
        temp += "Navie Time: "       + str(self.__naive_time)    + "\n"
        temp += "Tar. & Tro. Time: " + str(self.__tar_troj_time) + "\n"
        temp += "----------\n"
        return temp


    @property
    def naive_time(self):
        return self.__naive_time


    @property
    def tar_troj_time(self):
        return self.__tar_troj_time


    @property
    def V(self):
        return self.__V


    @property
    def E(self):
        return self.__E


    @property
    def density(self):
        return self.__density



def setup():
    #thread_cap = 3
    #thread_lock = BoundedSemaphore(value=thread_cap)
    graphs = []
    for i in range(ITERATIONS):
        V, E = generate_random_graph(DENSITY, LOWER, UPPER)
        graphs.append(Graph(V, E))
    for graph in graphs:
        #thread_lock.acquire()
        #t = Thread(target=graph.evaluate)
        #child = t.start()
        graph.evaluate()
    f = open("benchmark.txt", "w+")
    for graph in graphs:
        f.write(str(graph))
    f.close()


if __name__ == "__main__":
    ITERATIONS = 10
    LOWER      = 10
    UPPER      = 15
    DENSITY    = 0.3
    setup()
