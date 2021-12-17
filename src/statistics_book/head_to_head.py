import random


def get_random_scalar():
    return random.randint(1, 5)


def get_random_vector(m):
    return [get_random_scalar() for i in range(0, m)]


def compare(v1, v2):
    m1 = 0
    m = len(v1)
    for i1 in range(0, m):
        for i2 in range(0, m):
            if v1[i1] > v2[i2]:
                m1 += 1
    return m1 >= 0.5 * (m ** 2)


def single_run():
    m = 3
    a = get_random_vector(m)
    b = get_random_vector(m)
    c = get_random_vector(m)

    if compare(a, b) and compare(b, c) and compare(c, a):
        print('a', a)
        print('b', b)
        print('c', c)
        print('.' * 32)
        return True
    return False


def multi_run(n):
    for i in range(0, n):
        if single_run():
            break


if __name__ == '__main__':
    n = 1000000
    multi_run(n)
