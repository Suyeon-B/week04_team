from functools import lru_cache
import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())

@lru_cache(None)
def rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return rec(n-1)+rec(n-2)

print(rec(n))