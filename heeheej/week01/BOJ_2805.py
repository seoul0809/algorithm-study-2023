# ���� �ڸ���
# �޸�: 260112KB, �ð�: 528ms
# ����Ž��

import sys

input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

lo, hi = 0, max(heights)
result = 0
while lo + 1 < hi:
    sum = 0
    mid = (lo + hi) // 2
    for h in heights:
        temp = h - mid
        if temp > 0:
            sum += temp

    if M > sum:
        hi = mid
    else:
        lo = mid

print(lo)