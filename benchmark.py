from time import time
from naive import naive
from tarjan_trojanowski import maxset
from functions import generate_random_graph, density

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
        maxset(self.__V, self.__E)
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
    global graphs
    graphs = []
    for i in range(5):
        V, E = generate_random_graph(30)
        graphs.append(Graph(V, E))
        graphs[i].evaluate()
    f = open("benchmark.txt", "w+")
    for graph in graphs:
        f.write(str(graph))
    f.close()


if __name__ == "__main__":
    setup()
