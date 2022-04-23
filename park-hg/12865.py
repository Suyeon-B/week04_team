from functools import lru_cache
import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
w, v = [], []
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    w.append(W)
    v.append(V)

@lru_cache(None)
def rec(i, j):
    if j < 0:
        return -1e9
    if j == 0:
        return 0
    if i == 0:
        return 0
    return max(rec(i-1, j), rec(i-1, j-w[i-1])+v[i-1])

print(rec(len(w), K))