from typing import List


class Vertex:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __repr__(self) -> str:
        return f'{self.key}'

    def __hash__(self):
        return hash(self.key)


class Edge:
    def __init__(self, capacity: int, isResidual: bool) -> None:
        self.isResidual = isResidual
        self.capacity = capacity
        if not isResidual:
            self.flow = 0
            self.residual = capacity
        elif isResidual:
            self.flow = 0
            self.residual = 0
            # self.capacity = 0

    def __repr__(self) -> str:
        return f'{self.capacity} {self.flow} {self.residual} {self.isResidual}'


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
            self.neighbours[vertex1][vertex2] = [Edge(edge, False)]
        else:
            self.neighbours[vertex1][vertex2].append(Edge(edge, False))
        if vertex1 not in self.neighbours[vertex2]:
            self.neighbours[vertex2][vertex1] = [Edge(edge, True)]
        else:
            self.neighbours[vertex2][vertex1].append(Edge(edge, True))

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

    def getVertex(self, vertex_idx):
        return self.list[vertex_idx]

    def printGraph(self) -> None:
        n = self.order()
        print("------GRAPH------", n)
        for v in self.list:
            print(v, end=" -> ")
            nbrs = self.neighbours[v]
            for (j, w) in nbrs.items():
                for i in w:
                    print(j, i, end="; ")
            print()
        print("-------------------")

    def BFS(self, start) -> List:
        visited = []
        parent = [None for _ in range(self.order())]
        queue = [start]
        while queue:
            v = queue.pop(0)
            nbrs = self.neighbours[v]
            for key, items in nbrs.items():
                if key not in visited:
                    for i in items:
                        if i.residual > 0:
                            queue.append(key)
                            visited.append(key)
                            parent[self.getVertexIdx(key)] = v
        return parent

    def min_cap(self, start, end, parent):
        min_flow = float('inf')
        if parent[self.getVertexIdx(end)] is None:
            return 0
        current = end
        while current != start:
            parent_v = parent[self.getVertexIdx(current)]
            edges = self.neighbours[parent_v][current]
            for e in edges:
                if e.isResidual == False:
                    if min_flow > e.residual:
                        min_flow = e.residual
            current = parent[self.getVertexIdx(current)]
        return min_flow

    def path_augmentation(self, start, end, parent, min_flow):
        current = end
        while current != start:
            parent_v = parent[self.getVertexIdx(current)]
            edges = self.neighbours[parent_v][current]
            res_edges = self.neighbours[current][parent_v]
            for e in edges:
                if e.isResidual == False:
                    e.flow += min_flow
                    e.residual -= min_flow
            for e in res_edges:
                if e.isResidual == True:
                    e.residual += min_flow
            current = parent[self.getVertexIdx(current)]

    def ford_fulkerson(self, start, end):
        result = 0
        parent = self.BFS(start)
        min_flow = self.min_cap(start, end, parent)

        while min_flow > 0:
            result += min_flow
            self.path_augmentation(start, end, parent, min_flow)
            parent = self.BFS(start)
            min_flow = self.min_cap(start, end, parent)
        return result


def main():
    graf_0 = [('s', 'u', 2), ('u', 't', 1), ('u', 'v', 3),
              ('s', 'v', 1), ('v', 't', 2)]
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12),
              ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1),
              ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7),
              ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
    graphs = [graf_0, graf_1, graf_2, graf_3]
    for inx, g in enumerate(graphs):
        gl = Graph_List()
        for i in g:
            gl.insertEdge(Vertex(i[0]), Vertex(i[1]), i[2])
        print()
        # gl.printGraph()
        r = gl.ford_fulkerson(Vertex('s'), Vertex('t'))
        print(f'Maksymalny przepływ dla grafu {inx}: {r}')
        gl.printGraph()


if __name__ == "__main__":
    main()
