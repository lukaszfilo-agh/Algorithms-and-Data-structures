from typing import List
import numpy as np


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


class PointsSet:
    def __init__(self) -> None:
        self.points = []

    def __repr__(self) -> str:
        return f'{self.points}'

    def add(self, p: Point) -> None:
        self.points.append(p)

    def distance(self, p1: Point, p2: Point) -> str:
        return np.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def orientation(self, p1: Point, p2: Point, p3: Point) -> str:
        orient = (p2.y - p1.y)*(p3.x - p2.x) - (p3.y - p2.y)*(p2.x - p1.x)
        if orient > 0:
            return 'P'
        elif orient == 0:
            return 'W'
        else:
            return 'L'

    def find_first(self) -> Point:
        p = Point(np.inf, np.inf)
        for e in self.points:
            if e.x < p.x:
                p = e
            elif e.x == p.x:
                if e.y < p.y:
                    p = e
        return p

    def jarvis(self) -> List:
        start = self.find_first()
        result = [start]
        p = start
        while True:
            idx = self.points.index(p) + 1
            if idx > len(self.points) - 1:
                idx -= len(self.points)
            q = self.points[idx]
            for r in self.points:
                if r != q and p != r:
                    orient = self.orientation(p, q, r)
                    if orient == 'P':
                        q = r
            if q != start:
                result.append(q)
                p = q
            else:
                break
        return result

    def jarvis_v2(self) -> List:
        start = self.find_first()
        result = [start]
        p = start
        while True:
            idx = self.points.index(p) + 1
            if idx > len(self.points) - 1:
                idx -= len(self.points)
            q = self.points[idx]
            for r in self.points:
                if r != q and p != r:
                    orient = self.orientation(p, q, r)
                    if orient == 'P':
                        q = r
                    if orient == 'W':
                        d_pq = self.distance(p, q)
                        d_qr = self.distance(q, r)
                        d_pr = self.distance(p, r)
                        if d_pq + d_qr == d_pr:
                            q = r
            if q != start:
                result.append(q)
                p = q
            else:
                break
        return result


def main():
    points = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2),
              (0, 0), (2, 1), (2, 0), (4, 0)]

    p1s = PointsSet()
    p2s = PointsSet()
    for p in points:
        p1s.add(Point(p[0], p[1]))
    for p in points:
        p2s.add(Point(p[0], p[1]))
    j1 = p1s.jarvis()
    print(j1)
    j2 = p2s.jarvis_v2()
    print(j2)


if __name__ == "__main__":
    main()
