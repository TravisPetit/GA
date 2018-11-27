#from threading import *
import argparse
from time import time
from naive import naive
from tarjan_trojanowski import maxset
from functions import generate_random_graph, density, complement

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
        Ec = complement(self.__V, self.__E)
        maxset(self.__V, Ec)
        end = time()
        self.__tar_troj_time = round(end - start, 4)


    def __repr__(self):
        temp =  "Vertices: "       + str(len(self.__V))        + "\n"
        temp += "Edges: "          + str(len(self.__E))        + "\n"
        temp += "Graph Density: "  + str(self.__density)       + "\n"
        temp += "Navie Time: "     + str(self.__naive_time)    + "\n"
        temp += "Tar & Tro Time: " + str(self.__tar_troj_time) + "\n"
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
    f.write("INTERATIONS: " + str(ITERATIONS) + "\n")
    f.write("VERTEX LOWER BOUND: " + str(LOWER) + "\n")
    f.write("VERTEX UPPER BOUND: " + str(UPPER) + "\n")
    f.write("GRAPH AVERAGE DENSITY: " + str(DENSITY) + "\n")
    f.write("##########\n")
    for graph in graphs:
        f.write(str(graph))
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', help='Number of iterations', type=int, default=10)
    parser.add_argument('--l', help='Lower bound (min) of vertices', type=int, default=10)
    parser.add_argument('--u', help='Upper bound (max) of vertices', type=int, default=15)
    parser.add_argument('--d', help='Graph densities', type=int, default=0.6)
    args = parser.parse_args()
    ITERATIONS = args.i
    LOWER      = args.l
    UPPER      = args.u
    DENSITY    = args.d
    setup()
