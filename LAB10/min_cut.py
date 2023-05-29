import cv2
import numpy as np
from typing import List

class Vertex:
    def __init__(self, key, color=None):
        self.key = key
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
    I = cv2.imread('min_cut_seg_1.png',cv2.IMREAD_GRAYSCALE)
    YY, XX = I.shape
    scrible_FG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_FG[100:120, 100:120] = 255

    scrible_BG = np.zeros((YY,XX),dtype=np.ubyte)
    scrible_BG[0:20, 0:20] = 255

    I = cv2.resize(I,(32,32))
    scrible_BG = cv2.resize(scrible_BG,(32,32))
    scrible_FG = cv2.resize(scrible_FG,(32,32))


    hist_FG = cv2.calcHist([I],[0],scrible_FG,[256],[0,256])
    hist_FG = hist_FG/sum(hist_FG)

    hist_BG = cv2.calcHist([I],[0],scrible_BG,[256],[0,256])
    hist_BG = hist_BG/sum(hist_BG)

    vertices = []
    gl = Graph_List()
    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            v = Vertex(str(YY * i + j))
            v.color = I[i][j]
            vertices.append(v)
            gl.insertVertex(v)
    
    gl.printGraph()

if __name__ == "__main__":
    main()