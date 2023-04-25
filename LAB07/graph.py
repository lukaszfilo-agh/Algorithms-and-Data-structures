import polska
from typing import List


class Vertex:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)


class Graph_Matrix:
    def __init__(self) -> None:
        self.matrix = None
        self.list = None

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
                    edges.append((self.getVertex(i), self.getVertex(j)))
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


class Graph_List:
    def __init__(self) -> None:
        self.list = None
        self.neighbours = None

    def isEmpty(self) -> bool:
        if self.neighbours is None:
            return True
        else:
            return False

    def edges(self) -> List:
        edges = []
        for v1 in self.neighbours.keys():
            for v2 in self.neighbours[v1]:
                edges.append((v1, v2))
        return edges

    def size(self) -> int:
        return len(self.list)

    def insertVertex(self, vertex) -> None:
        if self.isEmpty():
            self.list = [vertex]
            self.neighbours = {}
            self.neighbours[vertex] = []
        else:
            if vertex not in self.list:
                self.list.append(vertex)
                self.neighbours[vertex] = []
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

        if vertex2 not in self.neighbours[vertex1]:
            self.neighbours[vertex1].append(vertex2)
        if vertex1 not in self.neighbours[vertex2]:
            self.neighbours[vertex2].append(vertex1)

    def deleteVertex(self, vertex) -> None:
        del (self.neighbours[vertex])
        for v1 in self.neighbours.keys():
            if vertex in self.neighbours[v1]:
                idx = self.neighbours[v1].index(vertex)
                del (self.neighbours[v1][idx])

        idx = self.getVertexIdx(vertex)
        del (self.list[idx])

    def deleteEdge(self, vertex1, vertex2) -> None:
        idx1 = self.neighbours[vertex1].index(vertex2)
        del (self.neighbours[vertex1][idx1])
        idx2 = self.neighbours[vertex2].index(vertex1)
        del (self.neighbours[vertex2][idx2])

    def getVertexIdx(self, vertex) -> int:
        return self.list.index(vertex)

    def getVertex(self, vertex_idx):
        return self.list[vertex_idx]


def main():
    gm = Graph_Matrix()
    for vertex in polska.graf:
        gm.insertEdge(vertex[0], vertex[1])
    gm.deleteVertex('K')
    gm.deleteEdge('W', 'E')

    gl = Graph_List()
    for vertex in polska.graf:
        gl.insertEdge(vertex[0], vertex[1])
    gl.deleteVertex('K')
    gl.deleteEdge('W', 'E')

    polska.draw_map(gm.edges())
    polska.draw_map(gl.edges())


if __name__ == "__main__":
    main()
