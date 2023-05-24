import numpy as np
from typing import List


class Vertex:
    def __init__(self, key, value=None, color=0):
        self.key = key
        self.value = value
        self.color = color

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self) -> str:
        return f'{self.key}'

    def __hash__(self):
        return hash(self.key)


class Graph_Matrix:
    def __init__(self) -> None:
        self.matrix = None
        self.list = None

    def order(self):
        if not self.isEmpty():
            return len(self.list)

    def isEmpty(self) -> bool:
        if self.matrix is None:
            return True
        else:
            return False

    def edges(self) -> List:
        edges = []
        for i in range(self.size()):
            for j in range(self.size()):
                if self.matrix[i][j] != 0:
                    edges.append(
                        (self.getVertex(i).key, self.getVertex(j).key))
        return edges

    def size(self) -> int:
        return len(self.list)

    def insertVertex(self, vertex) -> None:
        if self.matrix is None:
            self.matrix = [[0]]
            self.list = [vertex]
        else:
            if vertex not in self.list:
                self.list.append(vertex)
                for i in range(self.size() - 1):
                    self.matrix[i].append(0)
                self.matrix.append([0 for x in range(self.size())])
            else:
                print('Vertex already in graph')

    def insertEdge(self, vertex1, vertex2, egde=1) -> None:
        if not self.isEmpty():
            if vertex1 not in self.list:
                self.insertVertex(vertex1)
            if vertex2 not in self.list:
                self.insertVertex(vertex2)
        else:
            self.insertVertex(vertex1)
            self.insertVertex(vertex2)

        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)

        self.matrix[idx1][idx2] = egde
        self.matrix[idx2][idx1] = egde

    def deleteVertex(self, vertex) -> None:
        idx = self.getVertexIdx(vertex)
        del (self.list[idx])
        for i in range(self.size() + 1):
            del (self.matrix[i][idx])
        del (self.matrix[idx])

    def deleteEdge(self, vertex1, vertex2) -> None:
        idx1 = self.getVertexIdx(vertex1)
        idx2 = self.getVertexIdx(vertex2)
        self.matrix[idx1][idx2] = 0
        self.matrix[idx2][idx1] = 0

    def getVertexIdx(self, vertex) -> int:
        return self.list.index(vertex)

    def getVertex(self, vertex_idx):
        return self.list[vertex_idx]

    def printGraph(self) -> None:
        n = self.order()
        print("------GRAPH------", n)
        for v in self.list:
            print(v, end=" -> ")
            nbrs = self.matrix[self.getVertexIdx(v)]
            for idx, item in enumerate(nbrs):
                if item != 0:
                    print(self.list[idx], item, end="; ")
            print()
        print("-------------------")


def ullman(curr, matrix, used, gnp1, pnp2, izomorph):
    c.append(c[-1] + 1)
    if curr == matrix.shape[0]:
        mul = matrix @ (matrix @ gnp1).T
        if (pnp2 == mul).all():
            izomorph.append(matrix)
        return
    else:
        for i in range(len(matrix[curr])):
            if used[i] is False:
                used[i] = True
                matrix[curr][:] = 0
                matrix[curr][i] = 1
                ullman(curr + 1, matrix, used, gnp1, pnp2, izomorph)
                used[i] = False


def func(g1: Graph_Matrix, g2: Graph_Matrix):
    gnp1 = np.array(g1.matrix)
    pnp2 = np.array(g2.matrix)

    if gnp1.shape[0] > pnp2.shape[0]:
        m = np.zeros((pnp2.shape[0], gnp1.shape[0]))
    else:
        m = np.zeros((gnp1.shape[0], pnp2.shape[0]))

    used = [False for _ in range(m.shape[1])]
    izomorph = []
    ullman(0, m, used, gnp1, pnp2, izomorph)
    print(izomorph)


def main():
    global c
    c = [0]

    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1),
               ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
    g = Graph_Matrix()
    for i in graph_G:
        g.insertEdge(Vertex(i[0]), Vertex(i[1]))
    g.printGraph()
    p = Graph_Matrix()
    for i in graph_P:
        p.insertEdge(Vertex(i[0]), Vertex(i[1]))
    p.printGraph()

    func(g, p)
    print(c)


if __name__ == "__main__":
    main()
