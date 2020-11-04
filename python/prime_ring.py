#!/usr/bin/env python
# ‐*‐ coding:utf‐8 ‐*‐
"""code_info
@Time : 2020 2020/11/4 9:13
@Author : Oj
@File : prime_ring.py
"""


def IsPrimeNum(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def GetPrimeDic(n):
    Dic = {}
    for i in range(1, n + 1):
        Dic[i] = []

    for i in range(1, n + 1, 2):
        # even number
        for j in range(2, n + 1, 2):
            # odd number
            if IsPrimeNum(i + j):
                assert (j not in Dic[i])
                # {1:[2, 4, ...]}
                Dic[i] += [j]

                assert (i not in Dic[j])
                # {2:[1, 5, ...]}
                Dic[j] += [i]
    return Dic


def EnumPrimeRing(Dic, ringParts):
    # print ringParts
    tail = ringParts[-1]
    ringLen = len(ringParts)

    assert (ringLen <= len(Dic))

    if ringLen == len(Dic):
        head = ringParts[0]
        if tail in Dic[head]:
            print(ringParts)
        ringParts.pop()
        return

    for i in Dic[tail]:
        if i in ringParts:
            continue
        ringParts += [i]

        EnumPrimeRing(Dic, ringParts)
        if len(ringParts) > ringLen:
            ringParts.pop()
        assert (len(ringParts))
    return ringParts


if __name__ == "__main__":
    n = int(raw_input('input:'))
    primeDic = GetPrimeDic(n)
    primeRing = EnumPrimeRing(primeDic, [1])