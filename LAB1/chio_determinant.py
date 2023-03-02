from typing import List, Tuple
from copy import deepcopy


class Matrix:
    def __init__(self, arg, s=0) -> None:
        if isinstance(arg, Tuple):
            self.__rows = arg[0]
            self.__cols = arg[1]
            self.__matrix = [[s]*self.__cols for x in range(self.__rows)]
        if isinstance(arg, List):
            self.__matrix = self.c_matrix_lst(arg)[0]
            self.__rows = self.c_matrix_lst(arg)[1]
            self.__cols = self.c_matrix_lst(arg)[2]

    def c_matrix_lst(self, lst):
        matrix = [0] * len(lst)
        r = len(lst)
        c = len(lst[0])
        for i in range(len(lst)):
            matrix[i] = lst[i]
        return matrix, r, c

    def size(self):
        return self.__rows, self.__cols

    def __add__(self, other):
        if (self.__cols, self.__rows) != (other.__cols, other.__rows):
            raise Exception('Matrix size error')
        res = deepcopy(self)
        for i in range(res.__rows):
            for j in range(res.__cols):
                res[i][j] += other[i][j]
        return res

    def __mul__(self, other):
        if self.__cols != other.__rows:
            raise Exception('Matrix size error')
        res = Matrix((self.size()[0], other.size()[1]))
        for i in range(self.__rows):
            for j in range(other.__cols):
                for k in range(other.__rows):
                    res[i][j] += self[i][k] * other[k][j]
        return res

    def __getitem__(self, inx):
        return self.__matrix[inx]

    def __setitem__(self, inx, val):
        self.__matrix[inx] = val

    def __str__(self) -> str:
        s = ''
        for i in range(self.__rows):
            s += '|'
            for j in range(self.__cols):
                s += str(self.__matrix[i][j])
                if j == self.__cols - 1:
                    s += '| \n'
                else:
                    s += ' '
        return s


def transpose(matrix: Matrix) -> Matrix:
    res = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            res[j][i] = matrix[i][j]
    return res


def det_2x2(matrix: Matrix) -> float:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def chio_determinant(a11: float, matrix: Matrix) -> float:
    if matrix.size()[0] != matrix.size()[1]:
        raise Exception('Matrix size error')

    if matrix.size() == (2, 2):
        return a11 * det_2x2(matrix)

    size = matrix.size()[0]
    n_size = size - 1

    if matrix[0][0] == 0:
        for i in range(size):
            if matrix[i][0] != 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
                a11 *= -1

    n_a11 = a11 * 1 / (matrix[0][0] ** (size - 2))

    new_matrix = Matrix(((n_size, n_size)))

    for i in range(n_size):
        for j in range(n_size):
            det_m = Matrix([[matrix[0][0], matrix[0][j + 1]],
                           [matrix[i + 1][0], matrix[i+1][j + 1]]])
            new_matrix[i][j] = det_2x2(det_m)
    return chio_determinant(n_a11, new_matrix)


def det(matrix: Matrix):
    if matrix.size() == (2, 2):
        return det_2x2(matrix)
    else:
        return chio_determinant(1, matrix)


def main():
    m1 = Matrix([
        [5, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])

    print(det(m1))

    m2 = Matrix([
        [0, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ])

    print(det(m2))


if __name__ == '__main__':
    main()
