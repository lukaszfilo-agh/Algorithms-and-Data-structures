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
    p = path(parent)
    return lowest_cost, p


def string_compare_pd2(P, T):
    len_p = len(P)
    len_t = len(T)

    D = np.zeros((len_p, len_t), int)
    for x in range(len_p):
        D[x][0] = x
    parent = np.full((len_p, len_t), 'X')
    for x in range(1, len_p):
        parent[x][0] = 'D'

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
    end = int(np.where(D[-1] == min(D[-1]))[0])
    start = end - len_p + 2
    return start, end


def string_compare_pd3(P, T):
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
            inf = 0
            if T[j] != P[i]:
                inf = np.inf
            swap = D[i - 1][j - 1] + inf
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
    s = seq(parent, P)
    return s


def seq(parent, P):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    result = ''
    current = parent[i][j]
    while current != 'X':
        if current == 'D':
            i -= 1
        elif current == 'I':
            j -= 1
        elif current == 'M':
            result += P[i]
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
        current = parent[i][j]
    return result[::-1]


def path(parent):
    i = len(parent) - 1
    j = len(parent[0]) - 1
    result = ''
    current = parent[i][j]
    while current != 'X':
        result += current
        if current == 'D':
            i -= 1
        elif current == 'I':
            j -= 1
        else:
            i -= 1
            j -= 1
        current = parent[i][j]
    return result[::-1]


def sort_str(T):
    P = ' '
    new_t = T.replace(' ', '')
    list_T = []
    for e in new_t:
        list_T.append(e)
    list_T.sort()
    for e in list_T:
        P += str(e)
    return P



def main():
    P = ' kot'
    T = ' pies'
    result = string_compare_rec(P, T, len(P) - 1, len(T) - 1)
    print(result)

    P = ' biały autobus'
    T = ' czarny autokar'
    result, _ = string_compare_pd(P, T)
    print(result)

    P = ' thou shalt not'
    T = ' you should not'
    _, p = string_compare_pd(P, T)
    print(p)

    P = ' ban'
    T = ' mokeyssbanana'
    start, _ = string_compare_pd2(P, T)
    print(start)

    P = ' democrat'
    T = ' republican'
    s = string_compare_pd3(P, T)
    print(s)

    T = ' 243517698'
    P = sort_str(T)
    s = string_compare_pd3(P, T)
    print(s)

if __name__ == "__main__":
    main()
