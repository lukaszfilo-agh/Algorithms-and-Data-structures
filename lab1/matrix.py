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
        res = deepcopy(self)
        for i in range(res.__rows):
            for j in range(res.__cols):
                res[i][j] += other[i][j]
        return res

    def __mul__(self):
        pass

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


def main():
    m1 = Matrix(
        [[1, 0, 2],
        [-1, 3, 1]])

    m2 = Matrix(
        [[3, 1],
        [2, 1],
        [1, 0]])
    
    m3 = Matrix((2, 3), 1)

    print(transpose(m1))
    #print(m1*m2)


if __name__ == '__main__':
    main()