#!/usr/bin/python3
""" Write a script for prime game"""


def isWinner(x, nums):
    """Function that brings prime game to life"""
    if not nums or x < 1:
        return None
    n = max(nums)
   rm = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(pow(n, 0.5)) + 1):
        if not rm[i]:
            continue
        for j in range(i * i, n + 1, i):
            rm[j] = False
    rm[0] = rm[1] = False
    c = 0
    for i in range(len(rm)):
        if rm[i]:
            c += 1
        rm[i] = c
    plyr1 = 0
    for n in nums:
        plyr1 += rm[n] % 2 == 1
    if plyr1 * 2 == len(nums):
        return None
    if plyr1 * 2 > len(nums):
        return "Maria"
    return "Ben"
