import time


def naive(S, W):
    i = 0
    m = 0
    counter = 0
    idxs = []
    while m < len(S):
        counter += 1
        if S[m] == W[i]:
            if i == 0:
                start = m
            if i == len(W) - 1:
                idxs.append(start)
                i = 0
            i += 1
            m += 1
        else:
            m += 1
            i = 0
    return idxs, counter


def hash(word, N):
    d = 256
    q = 101  # liczba pierwsza
    hw = 0
    for i in range(N):  # N - to długość wzorca
        # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
        hw = (hw*d + ord(word[i])) % q
    return hw


def RabinKarp(S, pattern):
    hW = hash(pattern, len(pattern))
    M = len(S)
    N = len(pattern)
    h = 1
    d = 256
    q = 101  # liczba pierwsza
    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*d) % q
    counter = 0
    colisions = 0
    idxs = []
    hS = hash(S[0:N], len(S[0:N]))
    for m in range(M - N + 1):
        counter += 1
        if hS == hW:
            if S[m: m + N] == pattern:
                idxs.append(m)
            else:
                colisions += 1
        if m + N < len(S):
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
    return idxs, counter, colisions


def Knuth_Morris_Pratt_T(W):
    pos = 1
    cnd = 0
    T = [0 for _ in range(len(W))]
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    # T[pos] = cnd
    return T


def Knuth_Morris_Pratt(S, W):
    m = 0
    i = 0
    T = Knuth_Morris_Pratt_T(W)
    P = []
    counter = 0
    nP = 0
    while m < len(S):
        counter += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m - i)
                nP += 1
                i = 0
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return P, counter, T


def main():
    with open('lotr.txt', encoding='utf-8') as f:
        text = f.readlines()
    S = ' '.join(text).lower()
    t_start = time.perf_counter()
    patterns, counter = naive(S, 'time.')
    print(f'{len(patterns)}; {counter}')
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    patterns, counter, colisions = RabinKarp(S, 'time.')
    print(f'{len(patterns)}; {counter}; {colisions}')
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    patterns, counter, T = Knuth_Morris_Pratt(S, 'time.')
    print(f'{len(patterns)}; {counter}; {T}')
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


if __name__ == "__main__":
    main()
