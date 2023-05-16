from typing import List
import graf_mst as graf


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


class Graph_List:
    def __init__(self) -> None:
        self.list = None
        self.neighbours = None
        self.intree = set()
        self.distance = {}

    def order(self):
        if not self.isEmpty():
            return len(self.list)

    def isEmpty(self) -> bool:
        if self.neighbours is None:
            return True
        else:
            return False

    def edges(self) -> List:
        edges = []
        for v1 in self.neighbours.keys():
            for v2 in self.neighbours[v1]:
                edges.append((v1.key, v2.key))
        return edges

    def size(self) -> int:
        return len(self.list)

    def insertVertex(self, vertex) -> None:
        if self.isEmpty():
            self.list = [vertex]
            self.neighbours = {}
            self.neighbours[vertex] = {}
        else:
            if vertex not in self.list:
                self.list.append(vertex)
                self.neighbours[vertex] = {}
            else:
                print('Vertex already in graph')

    def insertEdge(self, vertex1, vertex2, edge) -> None:
        if not self.isEmpty():
            if vertex1 not in self.list:
                self.insertVertex(vertex1)
            if vertex2 not in self.list:
                self.insertVertex(vertex2)
        else:
            self.insertVertex(vertex1)
            self.insertVertex(vertex2)

        if vertex2 not in self.neighbours[vertex1]:
            self.neighbours[vertex1][vertex2] = edge
        if vertex1 not in self.neighbours[vertex2]:
            self.neighbours[vertex2][vertex1] = edge

    def deleteVertex(self, vertex) -> None:
        del (self.neighbours[vertex])
        for v1 in self.neighbours.keys():
            if vertex in self.neighbours[v1].keys():
                del (self.neighbours[v1][vertex])

        idx = self.getVertexIdx(vertex)
        del (self.list[idx])

    def deleteEdge(self, vertex1, vertex2) -> None:
        del (self.neighbours[vertex1][vertex2])
        del (self.neighbours[vertex2][vertex1])

    def getVertexIdx(self, vertex) -> int:
        return self.list.index(vertex)

    def getVertex(self, vertex_idx) -> Vertex:
        return self.list[vertex_idx]

    def printGraph(self) -> None:
        n = self.order()
        print("------GRAPH------", n)
        for v in self.list:
            print(v, end=" -> ")
            nbrs = self.neighbours[v]
            for (j, w) in nbrs.items():
                print(j, w, end=";")
            print()
        print("-------------------")

    def create_MST(self):
        mst = Graph_List()
        for i in self.list:
            mst.insertVertex(i)
        return mst

    def Prim(self):
        mst = self.create_MST()
        vertex = self.list[0]
        while vertex not in self.intree:
            self.intree.add(vertex)
            for neighbour in self.neighbours[vertex]:
                if vertex not in self.distance:
                    self.distance[vertex] = {}
                if neighbour not in self.intree:
                    self.distance[vertex][neighbour] = self.neighbours[vertex][neighbour]
            min_dist = float('inf')
            for key1 in self.distance.keys():
                for key2 in self.distance[key1]:
                    if key1 and key2 in self.intree:
                        continue
                    elif self.distance[key1][key2] < min_dist:
                        min_dist = self.distance[key1][key2]
                        min_key1 = key1
                        min_key2 = key2
            mst.insertEdge(min_key1, min_key2, min_dist)
            vertex = self.list[self.getVertexIdx(min_key2)]
        return mst


def main():
    g = Graph_List()
    for i in graf.graf:
        g.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
    prim = g.Prim()
    prim.printGraph()


if __name__ == "__main__":
    main()
