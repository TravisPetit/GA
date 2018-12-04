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


    def evaluate_times(self):
        """ Gets the times for the naive and tar & troj algorithms """
        self.evaluate_naive_time()
        self.evaluate_tar_troj_time()


    def evaluate_naive_time(self):
        """ Computes the time for the naive algorithm """
        start = time()
        naive(self.__V, self.__E)
        end = time()
        self.__naive_time = round(end - start, 4)


    def evaluate_tar_troj_time(self):
        """ Computes the time for the tarjan and trojanowsi's algorithm """
        start = time()
        Ec = complement(self.__V, self.__E)
        maxset(self.__V, Ec)
        end = time()
        self.__tar_troj_time = round(end - start, 4)


    def __repr__(self):
        temp =  "Vertices:       " + str(len(self.__V))        + "\n"
        temp += "Edges:          " + str(len(self.__E))        + "\n"
        temp += "Graph Density:  " + str(self.__density)       + "\n"
        temp += "Navie Time:     " + str(self.__naive_time)    + "\n"
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


def average(graphs):
    """ Returns the average runtime of the naive and Tar and Tro runtime """
    n_time = 0
    tnt_time = 0
    for graph in graphs:
        n_time   += graph.naive_time
        tnt_time += graph.tar_troj_time
    n_time   /= len(graphs)
    tnt_time /= len(graphs)
    return n_time, tnt_time


def setup():
    graphs = []
    for i in range(ITERATIONS):
        V, E = generate_random_graph(DENSITY, LOWER, UPPER)
        graphs.append(Graph(V, E))
        graphs[i].evaluate_times()

    n_time, tnt_time = average(graphs)
    n_time   = round(n_time, 4)
    tnt_time = round(tnt_time, 4)

    f = open("benchmark.txt", "w+")
    f.write("+------------------------------+\n")
    f.write("|Iterations: {0:18}|\n".format(ITERATIONS))
    f.write("|Vertex lower bound: {0:10}|\n".format(LOWER))
    f.write("|Vertex upper bound: {0:10}|\n".format(UPPER))
    f.write("|Average density: {0:13}|\n".format(round(DENSITY, 2)))
    f.write("+------------------------------+\n")

    f.write("+------------------------------+\n")
    f.write("|Average time naive: {0:10}|\n".format(n_time))
    f.write("|Average time Tar & Tro: {0:6}|\n".format(tnt_time))
    f.write("+------------------------------+\n\n")

    for graph in graphs:
        f.write(str(graph))
    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--i', help='Number of iterations', type=int, default=10)
    parser.add_argument('--l', help='Lower bound (min) of vertices', type=int, default=10)
    parser.add_argument('--u', help='Upper bound (max) of vertices', type=int, default=15)
    parser.add_argument('--d', help='Graph densities', type=float, default=0.6)
    args = parser.parse_args()
    ITERATIONS = args.i
    LOWER      = args.l
    UPPER      = args.u
    DENSITY    = args.d
    setup()
