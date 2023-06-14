import numpy as np


def string_compare_rec(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i

    swap = string_compare_rec(P, T, i - 1, j - 1) + (P[i] != T[j])
    insert = string_compare_rec(P, T, i, j - 1) + 1
    deletion = string_compare_rec(P, T, i - 1, j) + 1

    lowest_cost = min(swap, insert, deletion)

    return lowest_cost


def string_compare_pd(P, T):
    len_p = len(P)
    len_t = len(T)

    D = np.zeros((len_p, len_t), int)
    for x in range(len_p):
        D[x][0] = x
    for x in range(len_t):
        D[0][x] = x
    parent = np.full((len_p, len_t), 'X')
    for x in range(1, len_p):
        parent[x][0] = 'D'
    for x in range(1, len_t):
        parent[0][x] = 'I'

    for i in range(1, len_p):
        for j in range(1, len_t):
            swap = D[i - 1][j - 1] + (P[i] != T[j])
            insert = D[i][j - 1] + 1
            deletion = D[i - 1][j] + 1

            lowest_cost = min(swap, insert, deletion)
            D[i][j] = lowest_cost

            if lowest_cost == swap:
                if P[i] == T[j]:
                    parent[i][j] = 'M'
                else:
                    parent[i][j] = 'S'
            elif lowest_cost == insert:
                parent[i][j] = 'I'
            else:
                parent[i][j] = 'D'
    lowest_cost = D[len_p - 1][len_t - 1]
    return lowest_cost


def main():
    P = ' kot'
    T = ' pies'
    result = string_compare_rec(P, T, len(P) - 1, len(T) - 1)
    print(result)

    P = ' biały autobus'
    T = ' czarny autokar'
    result = string_compare_pd(P, T)
    print(result)


if __name__ == "__main__":
    main()
