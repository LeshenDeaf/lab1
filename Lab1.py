import numpy as np
from random import randint


def first():
    n = randint(10, 20)
    a = np.zeros((n, n), dtype=bool)
    a[0][1] = 1
    a[1][2] = 1
    a[2][0] = 1
    m = 3
    for i in range(3, n):
        a[i][randint(0, i - 1)] = 1
        a[randint(0, i - 1)][i] = 1
        m += 2

    n_w = [0] * n
    m_w = [0] * m
    for i in range(m):
        m_w[i] = randint(1, 20)
    for i in range(n):
        n_w[i] = randint(1, 20)

    out = open('out1.txt', 'w')
    out.write('{0} {1}\n'.format(n, m))
    k = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                out.write('{0} {1}, the weight of the edge is {2}\n'.format(i + 1, j + 1, m_w[k]))
                k += 1
    for i in range(n):
        out.write('{0}, weight is {1}\n'.format(i + 1, n_w[i]))
    out.close()


def second():
    n = randint(10, 20)
    m = 0
    a = np.zeros((n, n), dtype=np.int8)
    for i in range(n):
        connected = randint(1, n // 4)
        while connected > 0:
            chosen_dot = randint(0, n - 1)
            while chosen_dot == i or (a[i][chosen_dot] != 0 or a[chosen_dot][i] != 0):
                chosen_dot = randint(0, n - 1)
            weight = randint(1,5)
            a[i][chosen_dot] = weight
            a[chosen_dot][i] = weight
            m += 2
            connected -= 1

    n2_w = [0] * n

    for i in range(n):
        n2_w[i] = randint(1, 20)

    out = open('out2.txt', 'w')
    out.write('{0} {1}\n'.format(n, m))
    for i in range(n):
        for j in range(n):
            if a[i][j] != 0:
                out.write('{0} {1}, the weight of the edge is {2}\n'.format(i + 1, j + 1, a[i][j]))
    for i in range(n):
        out.write('{0}, weight is {1}\n'.format(i + 1, n2_w[i]))

    out.close()


def third():
    def connect(v, p, m):
        if v == 1:
            prev.append(0)
            return m
        if len(prev):
            eq = v // len(prev)
            for i in range(v):
                a[i + p][(i+1) % v + p] = randint(1, 7)
                m += 1
                prev.append(i + p)
                if i % 2:
                    a[i + p][prev[i//eq]] = randint(1, 7)
                    m += 1
                else:
                    a[prev[i // eq]][i + p] = randint(1, 7)
                    m += 1
        else:
            for i in range(v):
                a[i + p][(i+1) % v + p] = randint(1, 7)
                m += 1
                prev.append(i + p)
        return m

    n = randint(10,20)
    a = np.zeros((n, n), dtype=np.int8)
    n_bin = str(bin(n)[2:])[::-1]
    powers = []
    for i in range(len(n_bin)):
        if int(n_bin[i]):
            powers.append(2 ** i)

    pos = 0
    prev = []
    n_w = []
    m = 0
    for i in powers:
        m = connect(i, pos, m)
        prev = prev[i-1:]
        pos += i
    with open('out3.txt', 'w') as out:
        out.write('{0} {1}\n'.format(n, m))
        for i in range(n):
            for j in range(n):
                if a[i][j]:
                    out.write('{0} {1} weight of the edge is {2}\n'.format(i+1, j+1, a[i][j]))
        for i in range(n):
            n_w.append(randint(1, 7))
            out.write('{0} weight is {1}\n'.format(i + 1, n_w[-1]))


def fourth():
    n = randint(10, 20)
    m = 0
    a = np.zeros((n, n), dtype=np.int8)
    flag = [False] * n

    for i in range(n):
        con = randint(1, 4)
        probability = randint(i, n)
        if probability == i:
            a[i][0] = randint(1, 7)
            m += 1
        else:
            connected = 0
            for j in range(1, con + 1):
                if not flag[(i + j) % n]:
                    a[i][(i + j) % n] = randint(1, 7)
                    flag[(i + j) % n] = True
                    connected += 1
                    m += 1
                else:
                    continue
            if not connected:
                a[i][0] = randint(1, 7)
                m += 1

    n_w = [0] * n
    for i in range(n):
        n_w[i] = randint(1, 7)

    with open('out4.txt', 'w') as out:
        out.write('{0} {1}\n'.format(n, m))
        for i in range(n):
            for j in range(n):
                if a[i][j]:
                    out.write('{0} {1} weight of the edge is {2}\n'.format(i+1, j+1, a[i][j]))
        for i in range(n):
            out.write('{0} weight is {1}\n'.format(i+1, n_w[i]))
    return a


def fifth():
    def repeat(v, max, edges):
        a[v][(v+1) % (max + 1)] = randint(1, 7)
        edges += 1
        if max - v != v:
            a[max - v][v] = randint(1, 7)
            edges += 1
        return edges

    n = randint(10, 20)
    m = 0
    a = np.zeros((n, n), dtype=np.int8)
    for i in range(n):
        m = repeat(i, n-1, m)

    n_w = []
    for i in range(n):
        n_w.append(randint(1, 7))

    with open('out5.txt', 'w') as out:
        out.write('{0} {1}\n'.format(n, m))
        for i in range(n):
            for j in range(n):
                if a[i][j]:
                    out.write('{0} {1} weight of the edge is {2}\n'.format(i+1, j+1, a[i][j]))
        for i in range(n):
            out.write('{0} weight is {1}\n'.format(i+1, n_w[i]))

    return a


def main():
    first()
    second()
    third()
    fourth()
    fifth()
    print('Done!')


if __name__ == '__main__':
    main()
